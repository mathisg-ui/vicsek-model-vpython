# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:21:07 2021

@author: Mathisg-ui
"""

import numpy as np
import vpython as vp



#reput same parameters

N = 300 #number of cells
dt = 1 #time step
tmax = 100 #maximal time
#lcount = np.zeros(int(tmax/dt)) #list count
a = 0.2 #radius of the particle
L=20
cx = L #center of the cam
cy = L


data = np.loadtxt(r'\Users\hp\Desktop\python_code\Active_matter\viscek\yo.txt', delimiter=',')

bx, by, bo = data[:, 0], data[:, 1], data[:,2]


lX=[]
lY=[]
lo=[]

for i in range (int(tmax/dt)):
    xint=[]
    yint=[]
    oint=[]
    for j in range(N):  
        xint.append(bx[j+i*N])
        yint.append(by[j+i*N])
        oint.append(bo[j+i*N])
    lX.append(xint)
    lY.append(yint)
    lo.append(oint)
    
t=0
scene = vp.canvas(title='Cells simulation',width=1000, height=600,center=vp.vector(cx,cy,0), background=vp.color.black,autoscale = False)
vp.scene.camera.autoscale = False
#objs = [vp.sphere(pos=vp.vector(lX[int(t/dt)][i],lY[int(t/dt)][i],0),radius=a) for i in range(N)]
objs = [vp.arrow(pos=vp.vector(lX[int(t/dt)][i],lY[int(t/dt)][i],0), axis=vp.vector(np.cos(lo[int(t/dt)][i]),np.sin(lo[int(t/dt)][i]),0), shaftwidth=a) for i in range(N)]

c1 = vp.curve(vp.vec(L/2,L/2,0), vp.vec(3*L/2,L/2,0))
c2 = vp.curve(vp.vec(3*L/2,L/2,0), vp.vec(3*L/2,3*L/2,0))
c3 = vp.curve(vp.vec(3*L/2,3*L/2,0), vp.vec(L/2,3*L/2,0))
c4 = vp.curve(vp.vec(L/2,3*L/2,0), vp.vec(L/2,L/2,0))


vp.scene.camera.pos=vp.vector(0,0,10)
vp.scene.camera.axis=vp.vector(0,0,0)

while t<tmax:
    print(t)
    #vp.rate(0.1/dt)
    vp.rate(20)
    
    i=0
    for obj in objs:
        obj.pos = vp.vector(lX[int(t/dt)][i],lY[int(t/dt)][i],0)
        obj.axis = vp.vector(np.cos(lo[int(t/dt)][i]),np.sin(lo[int(t/dt)][i]),0)
        obj.color = vp.vector(np.cos(lo[int(t/dt)][i]),np.sin(lo[int(t/dt)][i]),np.sin(lo[int(t/dt)][i]))
        i=i+1
    t=t+dt


