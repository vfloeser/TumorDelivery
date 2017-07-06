##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   Plot temperature in 3D: dependent on space and time                                  #
#                                                                                        #
##########################################################################################

from parameters import *
from library_time import *

import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

mplt.rc('text', usetex=True)
mplt.rcParams.update({'font.size': 16})

def T(r, t):
    if r==0: 
        r=0.0001
    return (20 - (20. * sinh(3 * r))/(r * sinh(3)))*exp(-k2*t)+36
    
if __name__ == "__main__":
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)
    
    # create mesh
    R,Tem = np.meshgrid(r, t)
    
    zs = np.array([T(r,t) for r,t in zip(np.ravel(R), np.ravel(Tem))])
    Z = zs.reshape(R.shape)
    
    # create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(R, Tem, Z, cmap=cm.coolwarm)

    ax.set_xlabel(r'$r$')
    ax.set_ylabel(r'$t$')
    ax.set_zlabel(r'$T\quad [^\circ C]$')
    fig.colorbar(surf, shrink=0.5 )
    mplt.savefig('plots/temperature_3d.pdf', format='pdf') #save figure

    plt.show()
    
    
    
    
    
    