from parameters import *
from library_time import *
from paths import *

import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt
mplt.rc('text', usetex=True)
mplt.rcParams.update({'font.size': 16})
import logging, getopt, sys
import time
import os

##########################################################################################
#       C O N F I G U R A T I O N 
##########################################################################################

# activate ylim for w
var1 = u1
var3 = u3
var5 = u5
var10 = u10
var25 = u25
mode = "u" # u or w 

##########################################################################################
#       M A I N
##########################################################################################    
if __name__ == "__main__":

    if not os.path.exists('plots'):
        os.makedirs('plots')
        print('Created folder plots!')
    if not os.path.exists('plots/avg'):
        os.makedirs('plots/avg')
        print('Created folder plots/avg!')
        
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)
    
    avg_var1_r = np.zeros(Nr, dtype=np.float64)
    avg_var3_r = np.zeros(Nr, dtype=np.float64)
    avg_var5_r = np.zeros(Nr, dtype=np.float64)
    avg_var10_r = np.zeros(Nr, dtype=np.float64)
    avg_var25_r = np.zeros(Nr, dtype=np.float64)
        
    for i in range(Nr):
        # *1000000 for units
        avg_var1_r[i] = np.sum(var1[i,:])
        avg_var1_r[i] /= Nr*1000000
        avg_var3_r[i] = np.sum(var3[i,:])
        avg_var3_r[i] /= Nr*1000000
        avg_var5_r[i] = np.sum(var5[i,:])
        avg_var5_r[i] /= Nr*1000000
        #avg_var10_r[i] = np.sum(var10[i,:])
        #avg_var10_r[i] /= Nr*1000
        #avg_var25_r[i] = np.sum(var25[i,:])
        #avg_var25_r[i] /= Nr*1000
        
    mplt.plot(r/R, avg_var1_r, label=r'$\alpha = 1$')
    mplt.plot(r/R, avg_var3_r, label=r'$\alpha = 3$')
    mplt.plot(r/R, avg_var5_r, label=r'$\alpha = 5$')
    #mplt.plot(r/R, avg_var10_r, label=r'$\alpha = 10$')
    #mplt.plot(r/R, avg_var25_r, label=r'$\alpha = 25$')
    mplt.xlim(0,1)
##########################################################################################
    # lim for w, because some values dont make sense
    #mplt.ylim(1e-11,2e1)
    # lim for w, because some values dont make sense
##########################################################################################
    mplt.xlabel('$r$')
    mplt.ylabel('$'+mode+'\quad [\mu mol/cm^3]$')
    mplt.yscale('log')
    mplt.legend()
    mplt.tight_layout()
    mplt.savefig('plots/avg/avg_'+mode+'.pdf', format='pdf')
    mplt.show()