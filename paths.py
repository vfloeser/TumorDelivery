import numpy
import os, sys

pathname = os.path.dirname(__file__)

u1 = numpy.load(pathname+'/save/A1/u1498912109.216986.npy')
u3 = numpy.load(pathname+'/save/A3/u1498911842.760572.npy')
u5 = numpy.load(pathname+'/save/A5/u1498911690.450998.npy')
u10 = numpy.load(pathname+'/save/A10/u1498911542.675711.npy')
u25 = numpy.load(pathname+'/save/A25/u1498909385.61189.npy')

w1 = numpy.load(pathname+'/save/A1/w1498912109.216986.npy')
w3 = numpy.load(pathname+'/save/A3/w1498911842.760572.npy')
w5 = numpy.load(pathname+'/save/A5/w1498911690.450998.npy')
w10 = numpy.load(pathname+'/save/A10/w1498911542.675711.npy')
w25 = numpy.load(pathname+'/save/A25/w1498909385.61189.npy')