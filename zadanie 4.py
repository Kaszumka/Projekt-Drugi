# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 00:17:54 2023

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from numpy import linalg as LA
import math

gesty = pd.read_csv(r'C:\Users\kacpo\Desktop\gesty.csv')
gesty_zgiecia = gesty.iloc[:,[1,2,3,4,5,6,7,8,9,10]]
gesty_zgiecia = gesty_zgiecia[['P1_1','P1_2','P2_1','P2_2','P3_1','P3_2','P4_1','P4_2','P5_1','P5_2']].to_numpy()



gesty_1 = gesty_zgiecia[:,0]
gesty_2 = gesty_zgiecia[:,1]
gesty_3 = gesty_zgiecia[:,2]
gesty_4 = gesty_zgiecia[:,3]
gesty_5 = gesty_zgiecia[:,4]
gesty_6 = gesty_zgiecia[:,5]
gesty_7 = gesty_zgiecia[:,6]
gesty_8 = gesty_zgiecia[:,7]
gesty_9 = gesty_zgiecia[:,8]
gesty_10 = gesty_zgiecia[:,9]

def sensor_index():
    Maximum = []
    Minimum = []
    Difference = []
    for n in range(0,76):
        n += 1
        maximum_1 = np.max(gesty_1[0:76])
        maximum_2 = np.max(gesty_2[0:76])
        maximum_3 = np.max(gesty_3[0:76])
        maximum_4 = np.max(gesty_4[0:76])
        maximum_5 = np.max(gesty_5[0:76])
        maximum_6 = np.max(gesty_6[0:76])
        maximum_7 = np.max(gesty_7[0:76])
        maximum_8 = np.max(gesty_8[0:76])
        maximum_9 = np.max(gesty_9[0:76])
        maximum_10 = np.max(gesty_10[0:76])
        
        minimum_1 = np.min(gesty_1[0:76])
        minimum_2 = np.min(gesty_2[0:76])
        minimum_3 = np.min(gesty_3[0:76])
        minimum_4 = np.min(gesty_4[0:76])
        minimum_5 = np.min(gesty_5[0:76])
        minimum_6 = np.min(gesty_6[0:76])
        minimum_7 = np.min(gesty_7[0:76])
        minimum_8 = np.min(gesty_8[0:76])
        minimum_9 = np.min(gesty_9[0:76])
        minimum_10 = np.min(gesty_10[0:76])
        
        dane_max = {'Max_1': maximum_1,'Max_2':maximum_2,'Max_3': maximum_3,'Max_4':maximum_4,'Max_5': maximum_5,'Max_6':maximum_6
                ,'Max_7': maximum_7,'Max_8':maximum_8,'Max_9': maximum_9,'Max_10':maximum_10}
        dane_max = pd.Series(dane_max)
        dane_min = {'Min_1': minimum_1,'Min_2':minimum_2
                ,'Min_3': minimum_3,'Min_4':minimum_4,'Min_5': minimum_5,'Min_6':minimum_6,'Min_7': minimum_7,'Min_8':minimum_8
                ,'Min_9': minimum_9,'Min_10':minimum_10}
        dane_min = pd.Series(dane_min)
        
        df = pd.concat([dane_max,dane_min])
        Maximum = np.append(Maximum,df.iloc[0:10])
        Minimum = np.append(Minimum,df.iloc[10:20])
        Difference = np.subtract(Maximum,Minimum)
        Index = np.argmax(Difference)
               
        
    return(Index)

i = sensor_index()
print("Sensor z największym odchyleniem wartosci:",i)




   
k_1 = np.max(gesty_1[0:76])
k_2 = np.min(gesty_1[0:76])
K = k_1 - k_2

#To mialo posluzyc tez do wytyczenia punktow
#d = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)

y = range(76)
#Wytyczanie dystansu między roznica gestow a wartoscia K 
#d = []
#for x in range(0,76):
    #x += 1
    #distance = math.sqrt(((gesty_1[x]-K)**2)+((gesty_1[x+1]-K)**2))
    #d = np.append(d,distance)
#print(d)


t = np.linspace(0,0.5,75)
x = 100000 * np.sin(2*np.pi*2*t)
p2 = np.max(x[0:25])
p2 = [p2]
p2_y = [19]
p3 = np.min(x[40:70])
p3 = [p3]
p3_y = [56]
p1 = [gesty_1[0]]
p1_y = [0]
x_values = [p1,p3]
y_values = [p1_y,p3_y]
P1 = (p1,p1_y)
P1 = np.asarray(P1)
P2 = (p2,p2_y)
P2 = np.asarray(P2)
P3 = (p3,p3_y)
P3 = np.asarray(P3)
d=np.cross(P2.T-P1.T,P3.T-P1.T)/LA.norm(P2.T-P1.T)
d_y = [8]
d_x_values = [d,p2]
d_y_values = [d_y,p2_y]



plt.figure(0)
plt.plot(gesty_1[0:76],color = 'black')
plt.title("P1_1")
plt.plot(x,color = 'blue')
#plt.plot(y,d,marker = 'o')
plt.plot(p1,marker = 'o',color = 'red')
plt.plot(p2_y,p2,marker = 'o', color = 'red')
plt.plot(p3_y,p3,marker = 'o', color = 'red')
plt.plot(y_values,x_values,color = 'red')
plt.plot(d_y,d,marker = 'o', color = 'red')
plt.plot(d_y_values,d_x_values,color = 'black')
for i in range(0,len(d)): 
   plt.text(i+0.1,d[i],d[i])


p1_1 = [gesty_2[0]]
p1_y_1 = [0]
P1_1 = (p1_1,p1_y_1)
P1_1 = np.asarray(P1_1)

p2_1 = np.max(x[0:25])
p2_1 = [p2_1]
p2_y_1 = [19]
P2_1 = (p2_1,p2_y_1)
P2_1 = np.asarray(P2_1)

p3_1 = np.min(x[40:70])
p3_1 = [p3_1]
p3_y_1 = [56]
P3_1 = (p3_1,p3_y_1)
P3_1 = np.asarray(P3_1)

x_values_1 = [p1_1,p3_1]
y_values_1 = [p1_y_1,p3_y_1]

d_1=np.cross(P2_1.T-P1_1.T,P3_1.T-P1_1.T)/LA.norm(P2_1.T-P1_1.T)
d_y_1 = [6]
d_x_values_1 = [d_1,p2_1]
d_y_values_1 = [d_y_1,p2_y_1]

plt.figure(1)
plt.plot(gesty_2[0:76],color = 'black')
plt.title("P1_2")
plt.plot(x,color = 'blue')
plt.plot(p1_1,marker = 'o',color = 'red')
plt.plot(p2_y_1,p2_1,marker = 'o', color = 'red')
plt.plot(p3_y_1,p3_1,marker = 'o', color = 'red')
plt.plot(y_values_1,x_values_1,color = 'red')
plt.plot(d_y_1,d_1,marker = 'o', color = 'red')
plt.plot(d_y_values_1,d_x_values_1,color = 'black')
for i in range(0,len(d_1)): 
   plt.text(i+0.1,d_1[i],d_1[i])
   
print("dystans dla P1_1:",d)
print("dystans dla P1_2:",d_1)