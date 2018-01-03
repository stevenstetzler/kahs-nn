import numpy as np
import itertools
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import HTML
from random import *
import sys
import time

#Space dimension Parameters
LEN = 20
WID = 20
DEP = 1
A = LEN*WID
tau = 10
DT = .1
f = 4

RANK = 3
if RANK == 2:
    TOT = LEN*WID
    DIM = [LEN,WID]
    E= np.array([f,0])
else:
    TOT = LEN*WID*DEP
    DIM = [LEN,WID,DEP]
    E=np.array([0,0,-f])
#
# #Particle Parameters
# PROBSCAT=True
VEL = 1
SIZE = int(1*TOT)
Me = 1 #MeV/c (mass of electron)
Ce= 1
Se = .5 #

# #Scatterer Parameters
SSCAT = True
DETSCAT = True
if DETSCAT:
    SSCAT = False
P=1
SCATTERDENS = 10*LEN*WID #How many scatterers per unit area
SRAD=5


SURFSCAT=False
xct = 1
yct = 1
SCATCT = 5

# SCATCT = [-2*xct*np.pi/LEN,-2*yct*np.pi/WID]
SCATDEPTH = [5,5]
SCATDC = [0,0,0]
SCATDC[2] = (DEP)/1.5
RES = 4

DIAG = False
HBONE = False
HBF = 2
DIV= WID/HBF


#FOR PERIODIC SCATTERERS
#xct controls number of scatterers in  row, and yct controls spacing between rows
#Scatdepth controls the sharpness of the scatterers
    #Scatterers are only symmetric if the scattering counts are symmetric
    #Implementing a duty factor?
#Diag controls the diagonality of the wave
SCATPAT = "periodic"

#Sim Parameters
FPS = 30
FRAMES =150
#
# #Block Parameters
# LEG=1
# ANG=np.pi/2
# RAD = 1
#
# V="V"
# S="S"
# #y = cint(y)%DIV+((y%(2*DIV))/DIV)*(DIV-2*(y%DIV))
