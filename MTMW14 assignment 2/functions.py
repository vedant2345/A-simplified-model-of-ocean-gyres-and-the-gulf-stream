#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:34:19 2023

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
dx = d
dy = d


def v_on_ugrid(v):
    """ Interpolating values of 4 v's on u on the Arakawa C grid"""
    
    return (v[:-1, :-1] + v[1:, :-1] + v[:-1, 1:] + v[1:, 1:]) / 4
    

def u_on_vgrid(u):
    """Interpolating values of 4 u's on v on the Arakawa C grid"""

    return (u[:-1, :-1] + u[1:, :-1] + u[:-1, 1:] + u[1:, 1:]) / 4

def energy(ρ,H,u,v,η,d):
    
    E = 0.5*ρ*(H*(u**2 + v**2) + g*(η**2))
    Etotal = np.sum(E)*d*d
    
    return Etotal

def dη_dt(d,u,v):
    
    return (-H*(((u[:,1:] - u[:,:-1])/d) + ((v[1:,:] - v[:-1,:])/d) ))

def dudt(f0_u,d,η,v,u,τx):
    
    return (f0_u * v_on_ugrid(v) - g*((η[:,1:]-η[:,:-1])/d) - γ*u[:,1:-1] + τx/(ρ*H))

def dvdt(f0_v,d,η,v,u):
    
    return (-f0_v * u_on_vgrid(u) - g * ((η[1:,:]-η[:-1,:])/d) - γ * v[1:-1,:])