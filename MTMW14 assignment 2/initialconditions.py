#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:50:16 2023

@author: vedantvairagi
"""
import numpy as np

γ = 1E-6   #linear drag coefficient
L = 1E6   #size of domain
β = 1E-11 # beta plane constant
ρ = 1E3  #uniform density
H = 1E3    #resting depth of fluid
g = 10     #gravity
u = 100     #worst case velocity
f0 =1E-4   #coriolis for mid latitudes
τ0 = 0.2    #wind stress
size = 1e05
d = int(size/4) #grid spacing
#Rd = int(np.sqrt(g*H)/f)
totalsize = int(L/d) #size of phenomenon to determine regime
xpoints = totalsize
ypoints = totalsize
dt = 175


# x and y for analytical solution
xana = np.linspace(totalsize/2,L-(totalsize/2),totalsize)
yana = np.linspace(totalsize/2,L-(totalsize/2),totalsize)
Xana,Yana=np.meshgrid(xana,yana)

x1 = np.linspace(0,L,totalsize)
y1 = np.linspace(0,L,totalsize)
X1,Y1 = np.meshgrid(x1,y1)

x = np.linspace(0,L,totalsize+1)
y = np.linspace(0,L,totalsize+1)
X,Y = np.meshgrid(x,y)

u = np.zeros((xpoints,xpoints+1))
v = np.zeros((xpoints+1,xpoints))
η = np.zeros((xpoints,ypoints))
x = np.linspace(0,L,totalsize+1)
y = np.linspace(0,L,totalsize+1)
u1 = np.zeros((xpoints,xpoints+1))
v1 = np.zeros((xpoints+1,xpoints))
η_1 = np.zeros((xpoints,ypoints))

us = np.zeros((xpoints,xpoints+1))
vs = np.zeros((xpoints+1,xpoints))
ηs = np.zeros((xpoints,ypoints))
x = np.linspace(0,L,totalsize+1)
y = np.linspace(0,L,totalsize+1)
us1 = np.zeros((xpoints,xpoints+1))
vs1 = np.zeros((xpoints+1,xpoints))
ηs_1 = np.zeros((xpoints,ypoints))

uhalf = np.zeros((xpoints,xpoints+1))
vhalf = np.zeros((xpoints+1,xpoints))
ηhalf = np.zeros((xpoints,ypoints))
x = np.linspace(0,L,totalsize+1)
y = np.linspace(0,L,totalsize+1)
uhalf1 = np.zeros((xpoints,xpoints+1))
vhalf1 = np.zeros((xpoints+1,xpoints))
ηhalf_1 = np.zeros((xpoints,ypoints))

uehalf = np.zeros((xpoints,xpoints+1))
vehalf = np.zeros((xpoints+1,xpoints))
ηehalf = np.zeros((xpoints,ypoints))
x = np.linspace(0,L,totalsize+1)
y = np.linspace(0,L,totalsize+1)
uehalf1 = np.zeros((xpoints,xpoints+1))
vehalf1 = np.zeros((xpoints+1,xpoints))
ηehalf_1 = np.zeros((xpoints,ypoints))


yforu = np.linspace(d/2,L-d/2,totalsize)
yforv = np.linspace(d,L-d,totalsize-1)

#coriolis paramters

f0_u = np.array(np.tile(f0 + (β*yforu),(xpoints-1,1))).transpose()
f0_v = np.array(np.tile(f0 + (β*yforv),(ypoints,1))).transpose()

# wind forcing

τx = np.array(np.tile(τ0*-np.cos(np.pi*(yforu)/L),(xpoints-1,1))).transpose()
urk = np.zeros((xpoints,xpoints+1))
vrk = np.zeros((xpoints+1,xpoints))
ηrk = np.zeros((xpoints,ypoints))
k1 = np.zeros((xpoints,ypoints))
l1 = np.zeros((xpoints,xpoints+1))
m1 = np.zeros((xpoints+1,xpoints))
k2 = np.zeros((xpoints,ypoints))
l2 = np.zeros((xpoints,xpoints+1))
m2 = np.zeros((xpoints+1,xpoints))
k3 = np.zeros((xpoints,ypoints))
l3 = np.zeros((xpoints,xpoints+1))
m3 = np.zeros((xpoints+1,xpoints))
k4 = np.zeros((xpoints,ypoints))
l4 = np.zeros((xpoints,xpoints+1))
m4 = np.zeros((xpoints+1,xpoints))