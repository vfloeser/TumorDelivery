##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   Plot u or w, depending on configuration                                              #
#                                                                                        #
##########################################################################################

from parameters import *
from library_time import *
from paths import *

import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt
import logging, getopt, sys
import time
import os

plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 16})

##########################################################################################
#       C O N F I G U R A T I O N 
##########################################################################################

var = u1
al = 1   # 1, 3, 5, 10 or 25
mode = "u" # u or w


##########################################################################################
#       M A I N
##########################################################################################
if __name__ == '__main__':

    if not os.path.exists('save'):
        os.makedirs('save')
        print('Created folder save!')
    if not os.path.exists('plots'):
        os.makedirs('plots')
        print('Created folder plots!')
    if not os.path.exists('plots/uw'):
        os.makedirs('plots/uw')
        print('Created folder plots/uw!')
        
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)

    avg_var_t = np.zeros(Nt, dtype=np.float64)
    avg_var_r = np.zeros(Nr, dtype=np.float64)
    
    for i in range(Nt):
        avg_var_t[i] = np.sum(var[:,i])
        avg_var_t[i] /= Nt
    
    for i in range(Nr):
        avg_var_r[i] = np.sum(var[i,:])
        avg_var_r[i] /= Nr

    
    
    mplt.figure(111)
    for i in range (1,5):
        mplt.plot(r/R, var[:,int(i*Nt/4)-2], label='t = '+'{0:.2f}'.format(t[int(i*Nt/4)-2]))
    mplt.plot(r/R, var[:,0], label=r'$t$ = '+'{0:.2f}'.format(0))
    mplt.ylabel(r'$'+mode+'\quad [P mol/ccm]$')
    mplt.xlabel('r')
    mplt.xlim(0,1)
    mplt.legend()
    mplt.tight_layout()
    mplt.savefig('plots/uw/'+mode+str(al)+'.pdf', format='pdf')

    mplt.figure(222)
    mplt.plot(r/R, avg_var_r, label='avg')
    mplt.ylabel(r'$'+mode+'\quad [P mol/ccm]$')
    mplt.xlabel('r')
    mplt.xlim(0,1)
    mplt.legend()
    mplt.tight_layout()
    mplt.savefig('plots/uw/'+mode+str(al)+'.pdf', format='pdf')

    mplt.figure(333)
    mplt.plot(t, avg_var_t, label='avg')
    mplt.ylabel(r'$'+mode+'\quad [P mol/ccm]$')
    mplt.xlabel('t [h]')
    mplt.xlim(tmin,tmax)
    mplt.legend()
    mplt.tight_layout()
    mplt.savefig('plots/uw/'+mode+str(al)+'.pdf', format='pdf')

    mplt.figure(8)
    mplt.imshow(var,origin='lower')
    mplt.colorbar()
    
    
    mplt.show()