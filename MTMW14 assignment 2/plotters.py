#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:43:57 2023

@author: vedantvairagi
"""
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from initialconditions import *

def TaskC(etaana,uana,vana):
    
    fig, ax = plt.subplots(1, 3,figsize = (22,5),layout='constrained')

    c1 = ax[0].contourf(Xana,Yana,etaana)
    fig.colorbar(c1,ax=ax[0])
    ax[0].set_title('Surface elevation (m)')
    
    c2 = ax[1].contourf(uana)
    fig.colorbar(c2,ax=ax[1])
    ax[1].set_title('Zonal velocity')
    
    c3=ax[2].contourf(vana)
    fig.colorbar(c3,ax=ax[2])
    ax[2].set_title('Meridional velocity')

def TaskD1plot(etaval,uval,vval):
    
    fig, ax = plt.subplots(2, 2, figsize = (12,9),layout='constrained')
    fig.suptitle('Forward Backward time scheme for 1 day with dt = 175', fontsize=16)
    
    c1 = ax[0, 0].contourf(X1,Y1,etaval)
    ax[0, 0].set_xlabel('x (km)')
    ax[0, 0].set_ylabel('y (km)')
    fig.colorbar(c1,ax=ax[0,0])
    ax[0,0].set_title('Surface elevation (m)')
    
    
    c2 = ax[1, 0].plot(x,uval[0,:])
    ax[1, 0].set_xlabel('x direction(m)')
    ax[1, 0].set_ylabel('zonal velocity (m/s)')
    ax[1,0].set_title('Zonal Velocity')
    
    
    c2 = ax[0, 1].plot(y,vval[:,0])
    ax[0, 1].set_xlabel('y direction(m)')
    ax[0, 1].set_ylabel('Meridional velocity (m/s)')
    ax[0,1].set_title('Meridional velocity')
    
    
    c2 = ax[1, 1].plot(x1,etaval[20,:])
    ax[1, 1].set_xlabel('x direction(m)')
    ax[1, 1].set_ylabel('Surface elevation through the middle (m)')
    ax[1,1].set_title('η in the centre')
    
    plt.show()
    
def TaskD2plot(etavalsteady,uvalsteady,vvalsteady):
    
    fig, ax = plt.subplots(2, 2,figsize = (12,9),layout='constrained')
    fig.suptitle('Forward Backward time scheme at steady state (40 days) with dt = 175', fontsize=16)

    c1 = ax[0, 0].contourf(X1,Y1,etavalsteady)
    ax[0, 0].set_xlabel('x (km)')
    ax[0, 0].set_ylabel('y (km)')
    fig.colorbar(c1,ax=ax[0,0])
    ax[0,0].set_title('Surface elevation (m) at steady state')


    c2 = ax[1, 0].plot(x,uvalsteady[0,:])
    ax[1, 0].set_xlabel('x direction(m)')
    ax[1, 0].set_ylabel('zonal velocity (m/s)')
    ax[1,0].set_title('u at steady state')


    c2 = ax[0, 1].plot(y,vvalsteady[:,0])
    ax[0, 1].set_xlabel('y direction(m)')
    ax[0, 1].set_ylabel('Meridional velocity (m/s)')
    ax[0,1].set_title('v at steady state')


    c2 = ax[1, 1].plot(x1,etavalsteady[20,:])
    ax[1, 1].set_xlabel('x direction(m)')
    ax[1, 1].set_ylabel('Surface elevation through the middle (m)')
    ax[1,1].set_title('η in the centre at steady state')

    plt.show()
    
def energyplot(Energyval,days):
    
    nt = int(days*86400/dt)
    totaltime = days*86400
    timearray=np.linspace(1,totaltime,nt)
    fig, ax= plt.subplots()
    ax.plot(timearray/86400,Energyval)
    ax.set_xlabel('Time in days')
    ax.set_ylabel('Total energy (J)')
    plt.title('Energy')
    plt.show()
   
def RK4plot(etaRK,uRK,vRK):
    
    fig, ax = plt.subplots(2, 2,figsize = (12,9),layout='constrained')
    fig.suptitle('Runge Kutta 4th order scheme at steady state (40 days) with dt = 175', fontsize=16)
    
    c1 = ax[0, 0].contourf(X1,Y1,etaRK)
    ax[0, 0].set_xlabel('x (km)')
    ax[0, 0].set_ylabel('y (km)')
    fig.colorbar(c1,ax=ax[0,0])
    plt.title('Surface elevation (m) RK4')
    
    
    c2 = ax[1, 0].plot(x,uRK[0,:])
    ax[1, 0].set_xlabel('x direction(m)')
    ax[1, 0].set_ylabel('zonal velocity (m/s)')
    plt.title('u')
    
    
    c2 = ax[0, 1].plot(y,vRK[:,0])
    ax[0, 1].set_xlabel('y direction(m)')
    ax[0, 1].set_ylabel('Meridional velocity (m/s)')
    plt.title('v')
    
    
    c2 = ax[1, 1].plot(x1,etaRK[20,:])
    ax[1, 1].set_xlabel('x direction(m)')
    ax[1, 1].set_ylabel('Surface elevation through the middle (m)')
    plt.title('η in the centre')
    
    plt.show()
    
    