##########################################################################################
#                                G E N E R A L     I N F O                               #
#                                                                                        #
#   Calculation of Eq. (1) in Stapleton2013 using Finite Differences                     #
#   on r=[0,R]                                                                           #
#                                                                                        #
#   some variants:                                                                       #
#   -l INFO        shows status in command line                                          #
#   -v u           calculate variable u                                                  #
#   -v w           calculate variable w (speed up with given u using path)               #
#   --path=<PATH>  speed up using existing u                                             #
#                                                                                        #
##########################################################################################

from parameters import *
from library_time import *

import numpy as np
import pylab as plt
import matplotlib.pyplot as mplt
import logging, getopt, sys
import time
import os

 
if __name__ == "__main__":

    if not os.path.exists('save'):
        os.makedirs('save')
        print("Created folder save!")
    if not os.path.exists("save/A"+str(al)):
        os.makedirs("save/A"+str(al))
        print("Created folder save/A"+str(al)+"!")
    

########################################################################################
# some debug preferences                                                               #
########################################################################################
    t1 = time.gmtime()                                                                 #
    ts = time.time()                                                                   #
    opts = None                                                                        #
    var = 'u'                                                                          #
    path = None                                                                        #
                                                                                       #
    try:                                                                               #
        opts, args = getopt.getopt(sys.argv[1:], 'l:v:p', ['log=','var=', 'path='])    #
    except getopt.GetoptError:                                                         #
        quit()                                                                         #
                                                                                       #
    for opt, argu in opts:                                                             #
        if opt in ('-l', '--log'):                                                     #
            logging.basicConfig(level=argu)                                            #
        if opt in ('-v', '--var'):                                                     #
            var = str(argu)                                                            #
        if opt in ('-p', '--path'):                                                    #
            path = str(argu)                                                           #
########################################################################################
    
    
    C0 = np.zeros(Nr, dtype=np.float64)
    w0 = np.zeros(Nr, dtype=np.float64)
    t = np.linspace(tmin, tmax, Nt)
    r = np.linspace(0,R,Nr)
    
    if var=='u': #calculate only u
        print("Calculate u!\n\n\n")
        u = getU(C0, Nr, tmin, tmax, al)
    
        np.save("save/A"+str(al)+"/u"+str(ts)+".npy", u)
        
        avg_u_t = np.zeros(Nt, dtype=np.float64)
        avg_u_r = np.zeros(Nr, dtype=np.float64)
        for i in range(Nt):
            avg_u_t[i] = np.sum(u[:,i])
            avg_u_t[i] /= Nt
        
        for i in range(Nr):
            avg_u_r[i] = np.sum(u[i,:])
            avg_u_r[i] /= Nr
            
        t2 = time.gmtime()
        logging.info("SUMMARY")
        logging.info(time.strftime("Start time was %H:%M:%S", t1))
        logging.info(time.strftime("End time was %H:%M:%S", t2))
        logging.info("Nt = "+str(Nt))
        logging.info("Nr = "+str(Nr))
        logging.info("alpha = "+str(al))
        
    
        mplt.figure(4)
        mplt.imshow(u,origin='lower')
        mplt.colorbar()
    
    if var=='w': #calculate only w
        if path!=None:
            u = np.load(path)
        else:
            print("Calculate u first!\n\n\n")
            u = getU(C0, Nr, tmin, tmax, al)
            np.save("save/A"+str(al)+"/u"+str(ts)+".npy", u)
        
        print("Calculate w!\n\n\n")
        w = getW(u, w0, Nr, tmin, tmax, al)
        
        np.save("save/A"+str(al)+"/w"+str(ts)+".npy", w)
    
        avg_w_t = np.zeros(Nt, dtype=np.float64)
        avg_w_r = np.zeros(Nr, dtype=np.float64)
        
        for i in range(Nt):
            avg_w_t[i] = np.sum(w[:,i])
            avg_w_t[i] /= Nt
        
        for i in range(Nr):
            avg_w_r[i] = np.sum(w[i,:])
            avg_w_r[i] /= Nr
    
        
        t2 = time.gmtime()
        logging.info("SUMMARY")
        logging.info(time.strftime("Start time was %H:%M:%S", t1))
        logging.info(time.strftime("End time was %H:%M:%S", t2))
        logging.info("Nt = "+str(Nt))
        logging.info("Nr = "+str(Nr))
        logging.info("alpha = "+str(al))
        
    
        mplt.figure(8)
        mplt.imshow(w,origin='lower')
        mplt.colorbar()
    
    
    mplt.show()