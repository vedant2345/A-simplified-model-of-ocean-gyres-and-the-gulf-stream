#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:08:31 2023

@author: vedantvairagi
"""

import numpy as np
import matplotlib.pyplot as plt
from functions import *
from plotters import *

def numerical(d,u,v,η,u1,v1,η_1,xpoints,ypoints,X,Y,days,dt):
    
    nt = int(days*86400/dt)
    Eintime = np.zeros(nt)
    τx = τ0*-np.cos(np.pi*(Y)/L)
        
    for n in range(nt): 
        
        dudx = ((u[:,1:] - u[:,:-1])/d)
        dvdy = ((v[1:,:] - v[:-1,:])/d)
        η_1[:,:] = η[:,:] - H*dt*(dudx + dvdy)
        
        if (n%2 == 1):
                
            dη_1_dx = ((η[:,1:]-η[:,:-1])/d)
            dη_1_dy = ((η[1:,:]-η[:-1,:])/d)
            
            u1[:,1:-1] = u[:,1:-1] + (f0+(β*(Y[:-1,1:-1]+d/2)))*dt*v_on_ugrid(v)\
                    - g*dt*(dη_1_dx) - γ*dt*u[:,1:-1] + τx[:-1,1:-1]*dt/(ρ*H)
                    
                
            v1[1:-1,:] = v[1:-1,:] - (f0+(β*Y[1:-1,:-1]))*dt*u_on_vgrid(u1)\
                    - g*dt*(dη_1_dy) - γ*dt*v[1:-1,:]
            
                
        else:
            
        
            dη_1_dx = ((η_1[:,1:]-η_1[:,:-1])/d)
            dη_1_dy = ((η_1[1:,:]-η_1[:-1,:])/d)
            
            v1[1:-1,:] = v[1:-1,:] - (f0+(β*Y[1:-1,:-1]))*dt*u_on_vgrid(u1)\
                    - g*dt*(dη_1_dy) - γ*dt*v[1:-1,:]
            
            u1[:,1:-1] = u[:,1:-1] + (f0+(β*(Y[:-1,1:-1]+d/2)))*dt*v_on_ugrid(v)\
                    - g*dt*(dη_1_dx) - γ*dt*u[:,1:-1] + τx[:-1,1:-1]*dt/(ρ*H)
                
        u=u1
        v=v1
        η=η_1

        
    return u1,v1,η_1



