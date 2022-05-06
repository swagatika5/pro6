#Plotting various distribution functions(M-B, B-E, F-D) with energy at different temperature

import numpy as np
import matplotlib.pyplot as plt

e = 1.6e-19 #charge
k = 1.38e-23 #boltzmann const
u = 0 #ev  chemical potential it can be +ve,-ve or zero. for convenience we take it as zero

def f(E,T,a): #genral form for M-B,F-D,B-E distribution function
    return 1/((np.exp(((E-u)*e)/(k*T)))+a)

def plotgraph(x,y,xlabelstr,ylabelstr,titlestr):
        plt.plot(x, y, lw=3)
        plt.xlabel(xlabelstr, size=12)
        plt.ylabel(ylabelstr, size=12)
        plt.title(titlestr)
        
p = 1001
en = np.linspace(-0.5,0.5,p) #ev
t = np.linspace(100,1100,6)
y10 = np.zeros(p)
y11 = np.zeros(p)
y12 = np.zeros(p)
y13 = np.zeros(p)
y14 = np.zeros(p)
y15 = np.zeros(p)
y20 = np.zeros(p)
y21 = np.zeros(p)
y22 = np.zeros(p)
y23 = np.zeros(p)
y24 = np.zeros(p)
y25 = np.zeros(p)
y30 = np.zeros(p)
y31 = np.zeros(p)
y32 = np.zeros(p)
y33 = np.zeros(p)
y34 = np.zeros(p)
y35 = np.zeros(p)
for i in range(p):
    y10[i] = f(en[i],t[0],-1) #Bose-Einstein Distribution
    y11[i] = f(en[i],t[1],-1)
    y12[i] = f(en[i],t[2],-1)
    y13[i] = f(en[i],t[3],-1)
    y14[i] = f(en[i],t[4],-1)
    y15[i] = f(en[i],t[5],-1)
    y20[i] = f(en[i],t[0],0) #Maxwell-Boltzmann Distribution
    y21[i] = f(en[i],t[1],0)
    y22[i] = f(en[i],t[2],0)
    y23[i] = f(en[i],t[3],0)
    y24[i] = f(en[i],t[4],0)
    y25[i] = f(en[i],t[5],0)
    y30[i] = f(en[i],t[0],1) #Fermi-Dirac Distribution
    y31[i] = f(en[i],t[1],1)
    y32[i] = f(en[i],t[2],1)
    y33[i] = f(en[i],t[3],1)
    y34[i] = f(en[i],t[4],1)
    y35[i] = f(en[i],t[5],1)
plotgraph(en,y10,"Energy","Distribution Function","Bose-Einstein Distribution") 
plotgraph(en,y11,"Energy","Distribution Function","Bose-Einstein Distribution") 
plotgraph(en,y12,"Energy","Distribution Function","Bose-Einstein Distribution") 
plotgraph(en,y13,"Energy","Distribution Function","Bose-Einstein Distribution") 
plotgraph(en,y14,"Energy","Distribution Function","Bose-Einstein Distribution") 
plotgraph(en,y15,"Energy","Distribution Function","Bose-Einstein Distribution") 
plt.plot(en,y10)
plt.plot(en,y11)
plt.plot(en,y12)
plt.plot(en,y13)
plt.plot(en,y14)
plt.plot(en,y15)
plt.legend(["100k","300k","500k","700k","900k","1100k"]) 
plt.show()

plotgraph(en,y20,"Energy","Distribution Function","Maxwell-Boltzmann Distribution") 
plotgraph(en,y21,"Energy","Distribution Function","Maxwell-Boltzmann Distribution")
plotgraph(en,y22,"Energy","Distribution Function","Maxwell-Boltzmann Distribution")
plotgraph(en,y23,"Energy","Distribution Function","Maxwell-Boltzmann Distribution")
plotgraph(en,y24,"Energy","Distribution Function","Maxwell-Boltzmann Distribution")
plotgraph(en,y25,"Energy","Distribution Function","Maxwell-Boltzmann Distribution")
plt.plot(en,y20)
plt.plot(en,y21)
plt.plot(en,y22)
plt.plot(en,y23)
plt.plot(en,y24)
plt.plot(en,y25)
plt.legend(["100k","300k","500k","700k","900k","1100k"]) 
plt.show()

plotgraph(en,y30,"Energy","Distribution Function","Fermi-Dirac Distribution") 
plotgraph(en,y31,"Energy","Distribution Function","Fermi-Dirac Distribution")
plotgraph(en,y32,"Energy","Distribution Function","Fermi-Dirac Distribution")
plotgraph(en,y33,"Energy","Distribution Function","Fermi-Dirac Distribution")
plotgraph(en,y34,"Energy","Distribution Function","Fermi-Dirac Distribution")
plotgraph(en,y35,"Energy","Distribution Function","Fermi-Dirac Distribution")
plt.plot(en,y30)
plt.plot(en,y31)
plt.plot(en,y32)
plt.plot(en,y33)
plt.plot(en,y34)
plt.plot(en,y35)
plt.legend(["100k","300k","500k","700k","900k","1100k"]) 
plt.show()
