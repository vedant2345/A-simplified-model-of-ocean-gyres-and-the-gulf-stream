#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:19:18 2023

@author: dh837509
"""
import numpy as np
import matplotlib.pyplot as plt
from initialconditions import *
from plotters import *


def analytic(x,y,eta0):
    
    
    ϵ = γ/(L*β)
    a = (-1-np.sqrt(1+(2*np.pi*ϵ)**2))/(2*ϵ)
    b = (-1+np.sqrt(1+(2*np.pi*ϵ)**2))/(2*ϵ)
    
    def f1(x):
         return(np.pi*(1+((np.exp(a)-1)*np.exp(b*x) + ((1-np.exp(b))*np.exp(a*x)))/(np.exp(b)-np.exp(a))))
        
    
    def f2(x):
        return((np.exp(a)-1)*b*np.exp(b*x) + ((1-np.exp(b))*a*np.exp(a*x))/(np.exp(b) - np.exp(a)))
        

    u = -τ0/(np.pi*γ*ρ*H) * f1(x/L)*np.cos(np.pi*y/L)

    v = τ0/(np.pi*γ*ρ*H) * f2(x/L)*np.sin(np.pi*y/L)

    eta = eta0 + τ0/(np.pi*γ*ρ*H)*f0*L/g*(γ/(f0*np.pi)*f2(x/L)*np.cos(np.pi*y/L)+1/np.pi*f1(x/L)\
                                           *(np.sin(np.pi*y/L)*(1+β*y/f0)+β*L/(f0*np.pi)*np.cos(np.pi*y/L)))
    
    return u,v,eta
    

