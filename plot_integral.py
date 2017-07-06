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
var1 = w1
var3 = w3
var5 = w5
var10 = w10
var25 = w25
mode = "w" # u or w 

##########################################################################################
#       M A I N
##########################################################################################
if __name__ == "__main__":

    if not os.path.exists('plots'):
        os.makedirs('plots')
        print('Created folder plots!')
    if not os.path.exists('plots/integral'):
        os.makedirs('plots/integral')
        print('Created folder plots/integral!')
    
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)
    
    Ivar1  = np.zeros(Nt)
    Ivar3  = np.zeros(Nt)
    Ivar5  = np.zeros(Nt)
    Ivar10 = np.zeros(Nt)
    Ivar25 = np.zeros(Nt)
    for i in range(Nt):
        # /1000000 because of units
        Ivar1[i] = integrate(var1, i,r, Nt)/1000000
        Ivar3[i] = integrate(var3, i,r, Nt)/1000000
        Ivar5[i] = integrate(var5, i,r, Nt)/1000000
        Ivar10[i] = integrate(var10, i,r, Nt)/1000000
        Ivar25[i] = integrate(var25, i,r, Nt)/1000000
        
    mplt.plot(t, Ivar1, label=r'$\alpha = 1$')
    mplt.plot(t, Ivar3, label=r'$\alpha = 3$')
    mplt.plot(t, Ivar5, label=r'$\alpha = 5$')
    mplt.plot(t, Ivar10, label=r'$\alpha = 10$')
    mplt.plot(t, Ivar25, label=r'$\alpha = 25$')
    mplt.xlim(tmin, tmax)
    mplt.yscale('log')
    mplt.xlabel(r'$t\quad [h]$')
    mplt.ylabel(r'$\bar{'+mode+'}\quad [\mu mol]$')
##########################################################################################
    # lim for w, because some values dont make sense
    mplt.ylim(1e-11, 3e2) 
    # lim for w, because some values dont make sense
##########################################################################################
    mplt.legend(loc=1, bbox_to_anchor=(1, 0.9))
    mplt.tight_layout()
    mplt.savefig('plots/integral/int'+mode+'.pdf', format='pdf')
    mplt.show()