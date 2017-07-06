##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   This file defines the parameters used in the simulation provided by Stapleton2013    #
#   and Baxter 1989. Some of the parameters are variable. Their range will be given in   #
#   a comment.                                                                           #
#                                                                                        #
##########################################################################################
import numpy
##########################################################################################
#                                 S I M U L A T I O N   ( v a r )                        #
##########################################################################################
#p_inf = -2          #(-1) - (-3) mm Hg
tmin   = 0.0         # start time (h)
tmax   = 1.0         # end time (h)
Nr     = 200         # space steps  
R      = 1.0         # tumor radius
al     = 1           # fix alpha
p_v    = 10          # vascular pressure
k      = 3600*8.3e-6 # liposome clearance from plasma
k2     = 8.32        # exponential decay of temperature (lambda)
beta   = 1.3e7       # drug loading coeff of DOX
Vr     = 1e-3        # relation of tissue to blood volume
Cp     = 0.5         # initial concentration

##########################################################################################
#                              T U M O R       T I S S U E                               #
##########################################################################################
sigma = 0.19         # filtration reflection coeff
f     = 0.5          # fractional rate of liposome transport (theta_l)


##########################################################################################
#                          S U P P L E M E N T A L     I N F O                           #
##########################################################################################



##########################################################################################
#                                     M E 1 8 0
##########################################################################################
##fc = 3600*25.1e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
##K    = 3600*0.35e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
###p_v    = 5.0     # 10     nominal, vary between 5       and 30
##p_imax = 4.7
###R      = 4.99    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*46.5e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*0.15e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 5.0     # 10     nominal, vary between 5       and 30
#p_imax = 5.0
##R      = 5.1    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*28.1e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*0.15e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 5.8     # 10     nominal, vary between 5       and 30
#p_imax = 5.7
##R      = 5.3    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*6.3e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*10.8e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 9.2     # 10     nominal, vary between 5       and 30
#p_imax = 3.5
##R      = 4.75    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*26.5e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*2.9e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 6.2     # 10     nominal, vary between 5       and 30
#p_imax = 4.6
##R      = 1.7    # 0.5    nominal, vary between 1.7    and 42 (not possible)
##########################################################################################
#                                      H 5 2 0
##########################################################################################
#fc = 3600*13.5e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*995e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 11.2     # 10     nominal, vary between 5       and 30
#p_imax = 1.9
##R      = 130    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*11.7e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*999e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 11.2     # 10     nominal, vary between 5       and 30
#p_imax = 2.3
##R      = 110    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*93.4e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*0.12e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 5.2     # 10     nominal, vary between 5       and 30
#p_imax = 4.7
##R      = 45.6    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*46.9e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*0.13e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 5.1     # 10     nominal, vary between 5       and 30
#p_imax = 4.1
##R      = 45.3    # 0.5    nominal, vary between 1.7    and 42 
#
#fc = 3600*28.4e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*249e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 5.6     # 10     nominal, vary between 5       and 30
#p_imax = 1.7
##R      = 120    # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*38.8e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*448e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 7.8     # 10     nominal, vary between 5       and 30
#p_imax = 3.0
##R      = 1    # 0.5    nominal, vary between 1.7    and 42 (not possible)
##########################################################################################
#                                       V X 2
##########################################################################################
#fc = 3600*4405e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*651e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 42.4     # 10     nominal, vary between 5       and 30
#p_imax = 42.4
##R      = 1    # 0.5    nominal, vary between 1.7    and 42 (not possible)
#
#fc = 3600*70.8e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*998e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 38.1     # 10     nominal, vary between 5       and 30
#p_imax = 36.6
#R      = 42.5   # 0.5    nominal, vary between 1.7    and 42
#
#fc = 3600*1.4e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*541e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 17.5     # 10     nominal, vary between 5       and 30
#p_imax = 4.56
##R      = 1    # 0.5    nominal, vary between 1.7    and 42 (not possible)
#
#fc = 3600*1.1e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*988e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 26.3     # 10     nominal, vary between 5       and 30
#p_imax = 5.58
##R      = 1    # 0.5    nominal, vary between 1.7    and 42 (not possible)
#
#fc = 3600*963e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
#K    = 3600*133e-7  # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
##p_v    = 9.8     # 10     nominal, vary between 5       and 30
#p_imax = 9.81
##R      = 1    # 0.5    nominal, vary between 1.7    and 42 (not possible)
#
fc = 3600*1088e-7 # 2.5e-5 nominal, vary between 0.28e-5 and 180e-5 (*e-7)
K    = 3600*662e-7   # 7e-7   nominal, vary between 63e-7   and 0.1e-7 (*e-7)
#p_v    = 26.8     # 10     nominal, vary between 5       and 30
p_imax = 19.8
#R      = 0.78    # 0.5    nominal, vary between 1.7    and 42
##########################################################################################
V      = R**3*4/3*numpy.pi #tumor volume

##########################################################################################
#                            B A X T E R 1 9 8 9     I N F O                             #
##########################################################################################
pi_v       = 20
pi_i_n     = 10    #normal tissue
pi_i_t     = 15    #tumor  tissue
sigma_t_n = 0.91   #normal tissue
sigma_t_t = 0.82   #tumor  tissue

##########################################################################################
#                       S I M U L A T I O N    ( d o n ' t   c h a n g e )               #
##########################################################################################
Nt = int(Nr/R*(tmax-tmin)) # time steps
