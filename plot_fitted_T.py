##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   This file calculates the T(r) using nonlinear regression.                            #
#                                                                                        #
##########################################################################################
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 16})

def func(x, a, b, c):
    return (1 - 1/x * (np.sinh(c*x)/np.sinh(c)))*b + a
    
if __name__ == "__main__":
    x = np.array([0.00000000001,0.8,1])
    x1 = np.linspace(0.000000001,1,num=100, dtype=np.float64)
    y = np.array([50,44,36])
        
    plt.plot(x1, func(x1, 36., 20, 3)) # try and error
    plt.xlabel('r')
    plt.ylabel(r'$T\quad [^\circ C]$')
    plt.xlim(0,1)
    plt.ylim(36,50.05)
    plt.savefig('plots/temperature_2d.pdf', format='pdf')
    plt.show() 
    
    
    