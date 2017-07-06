##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   This file gives helping functions, so implemented equations taken from               #
#   Stapleton2013 and Baxter1989. The related equations are mentioned in the comments.   #
#                                                                                        #
##########################################################################################

from numpy import sqrt, sinh, cosh, exp, pi
import logging, getopt, sys
from parameters import *

# Stapleton2013, alpha (after (2) )
# should be between 0.5 and 150
# dimensionless ratio of vascular to interstitial permeability to fluid flow
#
# Parameters:
# V    : Volume
# fc : capillary filtration coeff (1/(mmHg * sec))
# K    : hydraulic conductivity, interstitial permeability (cm**2/(mmHg * sec))
def alpha(V):
    return V**(1./3) * sqrt(fc/(K*V))
    
    
    
# Baxter1989, (8a)
# dimensionless interstitial pressure in isolated tumor
# 
# Parameters:
# r : current radial position (cm)
# R : radius of tumor (cm)
# a : dimensionless ratio of vascular to interstitial permeability to fluid flow
def p_hat(r, a):
    if r==0:
        return 1 - a / sinh(a)
    r_hat = r/R
    return 1 - (sinh(a * r_hat) / (sinh(a) * r_hat))
    
    
# Baxter1989, (8a)
# interstitial pressure in isolated tumor (mmHg)
# 
# Parameters:
# phat  : dimensionless interstitial pressure in isolated tumor
# p_e   : effective pressure (mmHg)
# p_inf : surrounding pressure (mmHg)
def p_i(phat):
    # Baxter1989, (8a)
    # return phat*(p_e - p_inf) + p_inf
    #### own choice
    return p_imax * phat
    
    
    
# Baxter1989, (8b)
# dimensionless interstitial velocity in isolated tumor
#
# Parameters:
# r : current radial position (cm)
# R : radius of tumor (cm)
# a : dimensionless ratio of vascular to interstitial permeability to fluid flow
def v_hat(r, a):
    if r==0: 
        return 0.
    r_hat = r/R
    return (a * r_hat * cosh(a * r_hat) - sinh(a * r_hat)) / ((r_hat ** 2) * sinh(a))
    
    
# Baxter1989, (8b)
# interstitial velocity in isolated tumor (cm/sec)
#
# Parameters:
# vhat  : dimensionless interstitial velocity in isolated tumor
# R     : radius of tumor (cm)
# K     : hydraulic conductivity (cm**2/(mmHg * sec))
# p_e   : effective pressure (mmHg)
# p_inf : surrounding pressure (mmHg)
def v_i(vhat):
    #return K * (p_e - p_inf) * uhat / R
    return p_imax * K * vhat / R
    
    
# first half of Stapleton2013, (1)
#
# Parameters:
# r : current radial position (cm)
# V    : Volume
# c    : plasma concentration of the nanoparticle
# fc : capillary filtration coeff
# p_v  : vasculature pressure (mmHg)
# phat : dimensionless interstitial pressure in isolated tumor
# pr_i   : interstitial pressure in isolated tumor (mmHg)
# sigma: filtration reflection coefficient
def lambd(r, a, t):
    phat = p_hat(r, a)
    pr_i = p_i(phat)
    if (p_v - pr_i) <= 0.:
        return 0.
    return fc * (p_v - pr_i) * (1 - sigma) * c(t)
    
# heat transfer function
#
# Parameters:
# T : temperature
def h(T):
    if T <= 38:
        return 0
    elif T < 39:
        return (37.6 * T - 1428.8)/100
    else:
        return (1.76842105 * T  - 31.07368421)/100
        
# Temperature distribution
#
# Parameters:
# r: current normalized radial position (cm)
def T(r, t):
    if r==0: 
        r=0.00000001
    return (20 - (20. * sinh(3 * r))/(r * sinh(3))) * exp(-k2*t) + 36
    
# Concentration clearance
#
# Parameters: 
# k : liposome clearance rate
# Cp: initial liposome concentration
# t : time
def c(t):
    return Cp * exp(-k*t)
    
# Ablation coefficient (Gasselhuber2010)
#
# Parameters:
# t : time [h]
# r : radial position
def D(r, t):
    return 3600 * 6.7e-7 #cm^2/s
        

##########################################################################################
#                                                                                        #
#                           C A L C U L A T I O N   C O D E                              #
#                                                                                        #
##########################################################################################

# use Simpson rule 
def integrate(u, t, r, Nr):
    h = 1.*R/Nr/3
    I = 0.0
    for i in range(1,int(Nr/2)):
        I += u[2*i-2,t]*r[2*i-2]**2 + 4*u[2*i-1,t]*r[2*i-1]**2 + u[2*i,t]*r[2*i]**2
    return I*h*4*pi

# use Operator splitting as explained in the thesis to calculate u and w
def getU(C0, Nr, tmin, tmax, al):
    dr = 1.*R/(Nr)
    dt = dr
    Ntau = 100
    dtau = dt/Ntau
    
    logging.info("dt = "+str(dt))
    logging.info("Nt = "+str(Nt))
    logging.info("dr = "+str(dr))
    logging.info("Nr = "+str(Nr))
    logging.info("alpha = "+str(al))
    
    
    # divide r into N equidistant points
    r = numpy.linspace(0, R, Nr)
    # create matrix
    u = numpy.zeros((Nr, Nt), dtype=numpy.float64)
    #initialize matrix
    u[:,0] = C0
    
    
    # Donor Cell (Upwind) method 
    # for advection term: u_t + f*u_x = 0
    #
    #### variables for DC method
    n = dtau/(dr)
    m = f*n
    logging.info("m = "+str(m))
    
    # speedup: calculate h and v
    local_h = numpy.zeros(Nr)
    local_v = numpy.zeros(Nr)
    
    
    
    for t in range(Nt-1):
##########################################################################################
# C O N C E N T R A T I O N    L I P O S O M E S
##########################################################################################
        # in each time step solve System with Strang Splitting
        # Strang splitting: 0.5A + B + 0.5A
        un = numpy.zeros((Nr, Ntau), dtype=numpy.float64)
        un[:,0] = u[:,t]
        logging.info("t="+str(t))
        logging.debug("Calculate u(r,t)")
        
        for x in range(Nr):
            local_h[x] = h(T(r[x], (t+1)*dt))
            local_v[x] = v_i(v_hat(r[x], al))
            
        # create inner system 1
        for tau in range (int(Ntau/2)-1):
            for x in range(Nr):
##########################################################################################
# 0.5 RK
##########################################################################################
                it=100
                error=1
                
                #fix point iteration for backward euler
                #initial euler step
                un[x,tau+1] = un[x,tau] + dtau*(lambd(r[x], al, tau)/Vr - h(T(r[x], t*dt))*(un[x,tau]))
                while error > 1e-8:
                    u_n = un[x,tau] + dtau*(lambd(r[x], al, t+tau)/Vr - local_h[x]*(un[x,tau+1]))
                    error_v = un[x, tau+1]-u_n
                    error = numpy.sqrt(numpy.dot(error_v,error_v))
                    un[x,tau+1] = u_n
                    it-=1
                    if it < 0:
                        print("Too many iterations")
                        break
                
               
        logging.debug("RK1_u")
        # set last value as start value
        un[:,0] = un[:,int(Ntau/2)-2]
        
        
        #create inner system 2
        for tau in range (int(Ntau/2)-1):
            for x in range(1,Nr):
##########################################################################################
# DC
##########################################################################################
                # chain rule
                un[x,tau+1] = (1 - m*local_v[x])*un[x,tau] + m*local_v[x-1]*un[x-1, tau]
                
        logging.debug("DC2_u")
        
        #create inner system 2.2
        for tau in range(int(Ntau/2)-1, Ntau-1):
            for x in range(1,Nr):
##########################################################################################
# DC
##########################################################################################
                # chain rule
                un[x,tau+1] = (1 - m*local_v[x])*un[x,tau] + m*local_v[x-1]*un[x-1, tau]
                    
                    
        logging.debug("DC2.2_u")
        # set last value as start value
        un[:,int(Ntau/2)-1] = un[:,Ntau-1]
        

        #create inner system 1.2 
        for tau in range(int(Ntau/2)-1, Ntau-1):
            for x in range(Nr):
##########################################################################################
# 0.5 RK
##########################################################################################
                it=100
                error=1
                
                #fix point iteration for backward euler
                #initial euler step
                un[x,tau+1] = un[x,tau] + dtau*(lambd(r[x], al, tau)/Vr - h(T(r[x], t*dt))*(un[x,tau]))
                while error > 1e-8:
                    u_n = un[x,tau] + dtau*(lambd(r[x], al, t+tau)/Vr - local_h[x]*(un[x,tau+1]))
                    error_v = un[x, tau+1]-u_n
                    error = numpy.sqrt(numpy.dot(error_v,error_v))
                    un[x,tau+1] = u_n
                    it-=1
                    if it < 0:
                        print("Too many iterations")
                        break
              
            
        # set next value of u
        u[:,t+1] = un[:,-1]
        
        logging.debug("RK1.2_u")
    
    # fix boundary
    u[0,:] = u[1,:]
    
    
    return u
    
    
def getW(u, w0, Nr, tmin, tmax, al):
    dr = 1.*R/(Nr)
    dt = dr
    Ntau = 100
    dtau = dt/Ntau
    
    logging.info("dt = "+str(dt))
    logging.info("Nt = "+str(Nt))
    logging.info("dr = "+str(dr))
    logging.info("Nr = "+str(Nr))
    logging.info("alpha = "+str(al))
    
    
    # divide r into N equidistant points
    r = numpy.linspace(0, R, Nr)
    # create matrix
    w = numpy.zeros((Nr, Nt), dtype=numpy.float64)
    #initialize matrix
    w[:,0] = w0
    
    
    # Donor Cell (Upwind) method 
    # for advection term: u_t + f*u_x = 0
    #
    #### variables for DC method
    n = dtau/(dr)

    logging.info("n = "+str(n))
    
    # speedup: calculate h and v
    local_h = numpy.zeros(Nr)
    local_v = numpy.zeros(Nr)
    local_D = numpy.zeros(Nr)
        
        
    
    for t in range(Nt-1):
##########################################################################################
# C O N C E N T R A T I O N       D R U G
##########################################################################################
        # in each time step solve System with Strang Splitting
        # Strang splitting: 0.5A + 0.5B + C + 0.5B + 0.5A
        wn = numpy.zeros((Nr, Ntau), dtype=numpy.float64)
        wn[:,0] = w[:,t]
        
        for x in range(Nr):
            local_h[x] = h(T(r[x], t*dt))
            local_v[x] = v_i(v_hat(r[x], al))
            local_D[x] = D(r[x], t*dt)
        
        logging.info("t="+str(t))
        logging.debug("Calculate w(r,t)")
        
        
        # create inner system 1
        for tau in range (int(Ntau/2)-1):
            for x in range(Nr):
##########################################################################################
# 0.5 RK
##########################################################################################
                wn[x,tau+1] = wn[x,tau] + beta*local_h[x]*u[x,t]*(dtau)
                
                
        logging.debug("RK1_w")
        # set last value as start value
        
        wn[:,0] = wn[:,int(Ntau/2)-2]
        
        
        #create inner system 2
        for tau in range (int(Ntau/2)-1):
            for x in range(1,Nr):
##########################################################################################
# 0.5 DC
##########################################################################################
                # chain rule
                wn[x,tau+1] = (1 - n*local_v[x])*wn[x,tau] + n*local_v[x-1]*wn[x-1, tau]
        
        
        logging.debug("DC2_w")
        
        # set last value as start value
        wn[:,0] = wn[:,int(Ntau/2)-2]
        
        kappa = dtau/(2.0*dr**2)
       
        # create inner system 3
        for tau in range(1,Ntau):
##########################################################################################
# CRANK NICOLSON
##########################################################################################
            temp = wn[:, tau-1] # get values of previous time step
            b_r = numpy.zeros((Nr), dtype='float64')
            A = numpy.zeros((Nr,Nr), dtype='float64') # only inner values
            
            for x in range(1,Nr-1):
                A[x,x] = ( 1 + 2*kappa*local_D[x] )
                A[x, x+1 ] = -kappa*local_D[x+1]
                A[x, x-1] = -kappa*local_D[x-1]
                b_r[x] = kappa*local_D[x+1]*temp[x+1] + (1 - 2*kappa*local_D[x])*temp[x] + kappa*local_D[x-1]*temp[x-1]
            
            # use boundary values
            A[0,0] = ( 1 + 2*kappa*local_D[0])
            A[0, 1 ] = -kappa*local_D[1]
            A[Nr-1,Nr-1] = ( 1 + 2*kappa*local_D[Nr-1] )
            A[Nr-1, Nr-2] = -kappa*local_D[Nr-2]
            
            wn_new = numpy.linalg.solve(A,b_r) # solve system of equations
    
            # save values from this time step
            wn[:, tau] = wn_new
                    
        logging.debug("CN3_w")
        # set last value as start value
        wn[:,int(Ntau/2)-1] = wn[:,Ntau-1]
        
        
        #create inner system 2.2
        for tau in range(int(Ntau/2)-1, Ntau-1):
            for x in range(1,Nr):
##########################################################################################
# DC
##########################################################################################
                # chain rule
                wn[x,tau+1] = (1 - n*local_v[x])*wn[x,tau] + n*local_v[x-1]*wn[x-1, tau]
              
                    
        logging.debug("DC2.2")
        # set last value as start value
        wn[:,int(Ntau/2)-1] = wn[:,Ntau-1]
        

        #create inner system 1.2 
        for tau in range(int(Ntau/2)-1, Ntau-1):
            for x in range(Nr):
##########################################################################################
# 0.5 RK
##########################################################################################
                wn[x,tau+1] = wn[x,tau] + beta*local_h[x]*u[x,t]*(dtau)
                
        # set next value of w
        w[:,t+1] = wn[:,Ntau-1]
        
    # end of time loop
    
    w[0,:] = w[1,:]
    
    
    return w