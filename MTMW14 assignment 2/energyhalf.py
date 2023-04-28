#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:32:08 2023

@author: vedantvairagi
"""
import numpy as np
import matplotlib.pyplot as plt
from Analytical import *
from functions import *
from initialconditions import *
from plotters import *

days = 100
dt = 88
nt = int(days*86400/dt)

Eintime1 = np.zeros(nt)
    
def numericalenergyhalf(d,u,v,η,u1,v1,η_1,xpoints,ypoints,X,Y,Eintime):
    
    
    τx = τ0*-np.cos(np.pi*(Y)/L)
    
        
    for n in range(nt): 
        
        dudx = ((u[:,1:] - u[:,:-1])/d)
        dvdy = ((v[1:,:] - v[:-1,:])/d)
        η_1[:,:] = η[:,:] - H*dt*(dudx + dvdy)
        
        if (n%2 == 1):
                
            dη_1_dx = ((η_1[:,1:]-η_1[:,:-1])/d)
            dη_1_dy = ((η_1[1:,:]-η_1[:-1,:])/d)
            
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
        
        u_on_η = (u[:, 1:] + u[:, :-1]) / 2
        v_on_η = (v[1:, :] + v[:-1, :]) / 2
        Eintime[n]=energy(ρ,H,u_on_η,v_on_η,η,d)
        
    return u,v,η,Eintime





