# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:11:04 2021


@author: Mathisg-ui
"""


from sklearn.neighbors import NearestNeighbors



import numpy as np
import random
import matplotlib.pyplot as plt
import time
import random
import matplotlib.pyplot as plt


"""parameters value"""

N = 300#number of cells
v0 = 0.03 #desired velocity
L = 20.0 #size of the side of the square border
a=0.2 #size particle
tmin = 0 #initial time
dt = 1 #time step
tmax = 100 #maximal time
eta=0.1  #noise amplitude
max_voisin = 7
pola=0





def ini_ptcl():
    i=0 
    while i < N:
        x[i] = random.uniform(-L/2,L/2)
        y[i] = random.uniform(-L/2,L/2)
        
        
        test=True
        for j in range (0,i):
            dist = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if dist < 0.5*a and test:
                test=False
                i=i-1
        o[i]=random.uniform(0,2*np.pi-0.01)    
        i=i+1

def detect_ptcl():
    
    for i in range(N):
        for j in range(N):
            dij = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            newd = np.sqrt((x[i]-x[j]+L)**2+(y[i]-y[j])**2)
            if newd < dij:
                dij = newd
            newd = np.sqrt((x[i]-x[j]-L)**2+(y[i]-y[j])**2)
            if newd < dij:
                dij = newd
            newd = np.sqrt((x[i]-x[j])**2+(y[i]-y[j]+L)**2)
            if newd < dij:
                dij = newd
            newd = np.sqrt((x[i]-x[j])**2+(y[i]-y[j]-L)**2)
            
            if dij < 3*a:
                v[i][int(maxx[i])] = j
                maxx[i] = maxx[i]+1

def create_grid():
    global X,Y
    x1 = x+L
    x2 = x-L
    y1 = y+L
    y2 = y-L
    X = np.array([x,x,x,x1,x1,x1,x2,x2,x2])
    Y = np.array([y,y1,y2,y,y1,y2,y,y1,y2])
    X = X.flatten()
    Y = Y.flatten()

def detect_optimized():
    samples=[]
    samples = np.array([X,Y])
    samples = samples.transpose()
    
    neigh = NearestNeighbors(n_neighbors=max_voisin)
    neigh.fit(samples)
    for i in range(0,N):
        voisin = neigh.kneighbors([[x[i], y[i]]])
        for j in range(0,max_voisin):
            if voisin[0][0][j] < 4*a and voisin[0][0][j]>0. :
                v[i][int(maxx[i])] = voisin[1][0][j]%N  #store index neighboor of cell i
                maxx[i]=maxx[i]+1
                

def new_theta():
    for i in range(N):
        smean = 0
        cmean = 0
        
        if maxx[i]>0:
            
            for n in range(0,int(maxx[i])):
                smean = smean+np.sin(o[int(v[i][n])])
                cmean = cmean+np.cos(o[int(v[i][n])])
                omean = np.arctan(smean/cmean)
        else:
            omean=0
        
        o[i] = omean+random.uniform(-eta/2,eta/2)
        
def evolution_ptcl():
    for i in range(N):
        vx[i] = v0*np.cos(o[i])
        vy[i] = v0*np.sin(o[i])
        x[i] = x[i]+dt*vx[i]
        y[i] = y[i]+dt*vy[i]
        if x[i]>L/2:
            x[i] = x[i]-L
        if y[i]>L/2:
            y[i] = y[i]-L
        if x[i]<L/2:
            x[i] = x[i]+L
        if y[i]<L/2:
            y[i] = y[i]+L

def f_pola():
    global pola
    sc = 0
    ss = 0
    for i in range(N):
        sc = sc+np.cos(o[i])
        ss = ss+np.sin(o[i])
    pola = 1/N*np.sqrt(sc**2+ss**2)
        
    
               
        
            
       
def main():
    global x,y,ex,ey,vix,viy,o,lX,lY,t,v,maxx,vx,vy,X,Y
    ini_ptcl()
    t = tmin
    while t<tmax:
        v = np.zeros((N,N))  #table of neighboor with each cells along rows and its neighboor along columns
        maxx = np.zeros(N)
        #detect_ptcl()
        create_grid()
        detect_optimized()
        new_theta()
        evolution_ptcl()
        lX.append(x.tolist())
        lY.append(y.tolist())
        lo.append(o.tolist())
        print(t)
        t=t+dt



    
x = np.zeros(N)  #position
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)


vix = np.zeros(N) #velocity 
viy = np.zeros(N)

o = np.zeros(N) #theta


lX=[] #list for storing position at each step time
lY=[]
lo=[]

X=0  #grid for border condition
Y=0        


main()
    





f= open("yo.txt","w+")
for listX, listY, listo in zip(lX, lY, lo):   
    for xx, yy, oo in zip(listX,listY,listo):
        f.write('{0},{1},{2}\n'.format(xx,yy,oo))  #enlever \n
    
f.close()









