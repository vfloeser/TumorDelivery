##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   Plots the surface for w                                                              #
#   FIX THE TICKS FOR EACH PLOT                                                          #
#                                                                                        #
##########################################################################################

from parameters import *
from library_time import *
from paths import *

import scipy as sp
import scipy.integrate as integrate
import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
mplt.rc('text', usetex=True)
mplt.rcParams.update({'font.size': 16})

##########################################################################################
#       C O N F I G U R A T I O N 
##########################################################################################

var = w1
al = 1   # 1, 3, 5, 10 or 25
mode = "w" # u or w

##########################################################################################
#       M A I N
##########################################################################################    
if __name__ == "__main__":
    
    if not os.path.exists('plots'):
        os.makedirs('plots')
        print('Created folder plots!')
    if not os.path.exists('plots/surf'):
        os.makedirs('plots/surf')
        print('Created folder plots/surf!')
        
    # create grid
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)
    
    R,Tem = np.meshgrid(r, t)
    
    # plot   
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(Tem, R, var/1000000, cmap=cm.plasma, rstride=1, cstride=1,)

    ax.set_xlabel(r'$r$')
    ax.set_ylabel(r'$t$')
    ax.set_zlabel(r'$'+mode+'\quad [\mu mol/cm^3]$')
    cb = fig.colorbar(surf, shrink=0.5 , orientation='horizontal', pad=0.1, ticks=[0.0,5,10,15,20])
    cb.set_label(r'$[\mu mol/cm^3]$')
    mplt.tight_layout()
    mplt.savefig('plots/surf/surf_'+mode+'_a'+str(al)+'.pdf', format='pdf')

    plt.show()
    
    
    
    
    
    