# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 00:04:25 2023

"""

import pandas as pd
import matplotlib.pyplot as plt

gesty = pd.read_csv('gesty.csv')

P1_1=gesty['P1_1']
P1_2=gesty['P1_2']

P1_1 = list(P1_1)
P1_2 = list(P1_2)


P2_1=gesty['P2_1']
P2_2=gesty['P2_2']

P2_1 = list(P2_1)
P2_2 = list(P2_2)


P3_1=gesty['P3_1']
P3_2=gesty['P3_2']

P3_1 = list(P3_1)
P3_2 = list(P3_2)


P4_1=gesty['P4_1']
P4_2=gesty['P4_2']

P4_1 = list(P4_1)
P4_2 = list(P4_2)


P5_1=gesty['P5_1']
P5_2=gesty['P5_2']

P5_1 = list(P5_1)
P5_2 = list(P5_2)


plt.figure(1)
plt.title('1')
plt.plot(P1_1)
plt.plot(P1_2)

plt.figure(2)
plt.title('2')
plt.plot(P2_1)
plt.plot(P2_2)

plt.figure(3)
plt.title('3')
plt.plot(P3_1)
plt.plot(P3_2)

plt.figure(4)
plt.title('4')
plt.plot(P4_1)
plt.plot(P4_2)

plt.figure(5)
plt.title('5')
plt.plot(P5_1)
plt.plot(P5_2)


plt.figure(6)
plt.title('1, 2, 3, 4, 5')
# plt.xlim(204500,204600)
plt.plot(P1_1)
plt.plot(P1_2)
plt.plot(P2_1)
plt.plot(P2_2)
plt.plot(P3_1)
plt.plot(P3_2)
plt.plot(P4_1)
plt.plot(P4_2)
plt.plot(P5_1)
plt.plot(P5_2)
plt.plot((0,370000),(22000,22000),'r--')


def podmiana(P_oryg):
    P = P_oryg.copy()
    for i in range(len(P)):
        if P[i]>22000:
            print(i)
            print (P[i])
            print('')
            
            j = i
            while P[j]>22000:
                j += 1
                
            m = i
            while P[m-1] < P[m]:
                m -= 1
                
            n = j
            while P[n+1] < P[n]:
                n += 1
                
            for k in range(m,n):
                P[k] = (P[m]+P[n])/2
         
            print('')
            
    return P
           
 
def spr(P):
    print('spr')
    for i in range(len(P)):
        if P[i]>22000:
            print(i)
            print('ERROR')
            print (P[i])
            print(" ")

P1_1_zm = podmiana(P1_1)
P1_2_zm = podmiana(P1_2)

P2_1_zm = podmiana(P2_1)
P2_2_zm = podmiana(P2_2)

P3_1_zm = podmiana(P3_1)
P3_2_zm = podmiana(P3_2)

P4_1_zm = podmiana(P4_1)
P4_2_zm = podmiana(P4_2)

P5_1_zm = podmiana(P5_1)
P5_2_zm = podmiana(P5_2)

plt.figure(65)
plt.title('1, 2, 3, 4, 5 po podmianie')
# plt.xlim(204500,204600)
plt.plot(P1_1_zm)
plt.plot(P1_2_zm)
plt.plot(P2_1_zm)
plt.plot(P2_2_zm)
plt.plot(P3_1_zm)
plt.plot(P3_2_zm)
plt.plot(P4_1_zm)
plt.plot(P4_2_zm)
plt.plot(P5_1_zm)
plt.plot(P5_2_zm)
plt.plot((0,370000),(22000,22000),'r--')

print('spr(P1_1_zm)')
spr(P1_1_zm)

print('spr(P1_2_zm)')
spr(P1_2_zm)


print('spr(P2_1_zm)')
spr(P2_1_zm)

print('spr(P2_2_zm)')
spr(P2_2_zm)


print('spr(P3_1_zm)')
spr(P3_1_zm)

print('spr(P3_2_zm)')
spr(P3_2_zm)


print('spr(P4_1_zm)')
spr(P4_1_zm)

print('spr(P4_2_zm)')
spr(P4_2_zm)


print('spr(P5_1_zm)')
spr(P5_1_zm)

print('spr(P5_2_zm)')
spr(P5_2_zm)


gesty1 = gesty.copy()

gesty1['P1_1'] = P1_1_zm
gesty1['P1_2'] = P1_2_zm

gesty1['P2_1'] = P2_1_zm
gesty1['P2_2'] = P2_2_zm

gesty1['P3_1'] = P3_1_zm
gesty1['P3_2'] = P3_2_zm

gesty1['P4_1'] = P4_1_zm
gesty1['P4_2'] = P4_2_zm

gesty1['P5_1'] = P5_1_zm
gesty1['P5_2'] = P5_2_zm


gesty1.to_csv('gesty_naprawione.csv')