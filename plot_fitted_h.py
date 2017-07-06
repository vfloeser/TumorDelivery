##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   This file calculates the function h(T) using nonlinear regression.                   #
#                                                                                        #
##########################################################################################
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 16})

def f0(x):
    return 0*x
    
def func(x, a, b, c, d, e): # biexponential fitting
    return a * np.exp(-b * x) + c * np.exp(d * x)+ e
    
def func2(x, m, b): # linear fitting
    return m*x + b
    
def func3(x, a, b, c, d): # 4PL Regression
    return d + ( a-d )/ (1 + (x/c)**b)
    
def T37(x):
    return x*16
    
def T38(x):
    return x*17.6
    
def T39(x):
    return x*37.6
    
def T40(x):
    return x*40
    
def T47(x):
    return x*52
    
def lamb(x):
    return np.log(2)/x

    
if __name__ == "__main__":
    x = np.array([37,38, 39, 40, 47])
    
    x1 = np.linspace(36,49,num=100, dtype=np.float64)
    x2 = np.linspace(39,47, num=50)
    x3 = np.linspace(36,38, num = 3)
    t = [ 1., 1.25, 2.5]
    #y = np.array([0,0, 19.23, 31.25, 47.62])
    y = np.array([0,0, 37.6, 40, 52])
    
    plt.figure(1)
    xt = np.linspace(0,1.25,num=100)
    plt.plot(xt, T37(xt), label=r'$37^\circ C$')
    plt.plot(xt, T38(xt), label=r'$38^\circ C$')
    plt.plot(xt, T39(xt), label=r'$39^\circ C$')
    plt.plot(xt, T40(xt), label=r'$40^\circ C$')
    plt.plot(xt, T47(xt), label=r'$47^\circ C$')
    plt.xlabel(r'$t\quad[s]$')
    plt.ylabel(r'$Rate\ of\ DOX\quad [\%]$')
    plt.legend(loc=2) 
    plt.xlim(0,1.25)
    plt.tight_layout()
    plt.ylim(0,100)
    plt.savefig('plots/linear_gasselhuber.pdf', format='pdf')
    plt.title("Linear Fitting Gasselhuber")
    
    ######################################################################################
    # HERE STARTS THE ACTUAL CURVE FITTING, but we rather want linear fitting
    # popt2 = curve_fit(func2, x[2:], y[2:])
    # popt3 = curve_fit(func3, x, y)
    # poptt = curve_fit(func2, [39,40,47], lamb(t))
    # print(popt2[0])
    # print(popt3[0])
    # print(poptt[0])
    # print("\nCandidate: 4PL Regression!!!")
    ######################################################################################
    plt.figure(2)
    
    plt.plot(x, y/100, 'o', label="exact points")
    plt.plot(x2,func2(x2, 1.76842105, -31.07368421)/100, 'g', label="Linear")
    plt.plot(x3,f0(x3), 'g')
    plt.plot([38,39],[0,0.376], 'g--')
   

    plt.xlim(36,49)
    plt.ylim(-0.005,0.60)
    plt.xlabel(r'$T\quad [^\circ C]$')
    plt.ylabel(r'$h\quad [1/s]$')
    plt.tight_layout()
    plt.savefig('plots/linear_fitting_h.pdf', format='pdf')
    
    plt.show()
    
    
    