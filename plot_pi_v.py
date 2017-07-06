##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   Some plots                                                                           #
#                                                                                        #
#                                                                                        #
##########################################################################################

from parameters import *
from library_time import *

import scipy as sp
import scipy.integrate as integrate
import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt

plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 16})

    
if __name__ == '__main__':
    Nr = 500
    r = np.linspace(0,R,Nr)
    
    al = [1,3,5,10,25] #alpha(V),
    for count in range(5):
        a = al[count]
        y_pi = np.zeros(Nr)
        y_ph = np.zeros(Nr)
        y_vi = np.zeros(Nr)
        y_vh = np.zeros(Nr)
        y_pv = np.zeros(Nr)
        y_v = np.ones(Nr)*p_v
          
        for i in range(Nr):
            y_ph[i] = p_hat(r[i], a)
            y_pi[i] = p_i(y_ph[i])
            y_vh[i] = v_hat(r[i],a)
            y_vi[i] = v_i(y_vh[i])
            y_pv[i] = p_v - y_pi[i]

        mplt.figure(1)
        mplt.xlabel(r'r')
        mplt.ylabel('dimensionless interstitial pressure')
        mplt.plot(r/R, y_ph, label=r'$\alpha$ = '+str(a))
        mplt.xlim(0,1)
        mplt.ylim(0,1)
        mplt.tight_layout()
        mplt.legend(loc=3, bbox_to_anchor=(0, 0.2))
        
        mplt.figure(11)
        mplt.xlabel(r'r')
        mplt.ylabel(r'$p_i(r)\quad [mmHg]$')
        mplt.xlim(0,1)
        mplt.tight_layout()
        mplt.plot(r/R, y_pi, label=r'$\alpha$ = '+str(a))
        mplt.legend(loc=2)

    
        mplt.figure(2)
        mplt.xlabel(r'r')
        mplt.ylabel(r'$v(r)\quad [cm/s]$')
        mplt.xlim(0,1)
        mplt.ylim(0,25)
        mplt.tight_layout()
        mplt.plot(r/R, y_vi, label=r'$\alpha$ = '+str(a))
        mplt.legend(loc=2)
        
        mplt.figure(3)
        mplt.ylabel('$p_v - p_i\quad [mmHg]$')
        mplt.xlabel(r'r')
        mplt.ylim(0,p_v)
        mplt.xlim(0,1)
        mplt.tight_layout()
        mplt.plot(r/R, y_pv, label=r'$\alpha$ = '+str(a))
        mplt.legend()
    
    # after loop: save figures
    mplt.figure(3)
    mplt.savefig('plots/pv-pi.pdf', format='pdf')
    mplt.figure(2)
    mplt.savefig('plots/velocity.pdf', format='pdf')

    mplt.show()