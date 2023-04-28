#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:36:38 2023

@author: dh837509
"""
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from initialconditions import *
from plotters import *
import time

def Rungekutta(η,u,v,d,dt,days):
    
    nt = int(days*86400/dt)
    
    
    for n in range(nt):
        
        k1 = dη_dt(d,u,v)      # for η
        l1[:,1:-1] = dudt(f0_u,d,η,v,u,τx) # for u
        m1[1:-1,:] = dvdt(f0_v,d,η,v,u) # for v

        k2 = dη_dt(d,u+(l1*dt)/2,v+(m1*dt)/2)  # for η
        l2[:,1:-1] = dudt(f0_u,d,η+(k1*dt)/2,v+(m1*dt)/2,u+(l1*dt)/2,τx) # for u
        m2[1:-1,:] = dvdt(f0_v,d,η+(k1*dt)/2,v+(m1*dt)/2,u+(l1*dt)/2) # for v
        
        k3 = dη_dt(d,u+(l2*dt)/2,v+(m2*dt)/2)  # for v
        l3[:,1:-1] = dudt(f0_u,d,η+(k2*dt)/2,v+(m2*dt)/2,u+(l2*dt)/2,τx) # for u
        m3[1:-1,:] = dvdt(f0_v,d,η+(k2*dt)/2,v+(m2*dt)/2,u+(l2*dt)/2) # for v
        
        k4 = dη_dt(d,u+(l3*dt),v+(m3*dt))  #for η
        l4[:,1:-1] = dudt(f0_u,d,η+(k3*dt),v+(m3*dt),u+(l3*dt),τx) # for u
        m4[1:-1,:] = dvdt(f0_v,d,η+(k3*dt),v+(m3*dt),u+(l3*dt)) # for v
        
        η =  η + (dt/6) * (k1+ 2*k2 + 2*k3 + k4)    # for η
        u =  u + (dt/6) * (l1+ 2*l2 + 2*l3 + l4)    # for u
        v =  v + (dt/6) * (m1+ 2*m2 + 2*m3 + m4)    # for v
        
    return η,u,v
    