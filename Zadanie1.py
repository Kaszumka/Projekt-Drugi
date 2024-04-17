#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
x=str(input('podaj słowo małymi literami: '))
A=pd.read_csv("C:/Users\huber\OneDrive\Pulpit\PROJEKT 3 SEMESTR\gesty.csv")


a=A.sample(frac=1)
wycinanie=x
if wycinanie=='a':
    B=a[a['sign']=='a ']
    a1=B['P1_1']
    a1=a1.head(n=75)   
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='b':
    B=a[a['sign']=='b ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='c':
    B=a[a['sign']=='c ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='e':
    B=a[a['sign']=='e ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='i':
    B=a[a['sign']=='i ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='l':
    B=a[a['sign']=='l ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='m':
    B=a[a['sign']=='m ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='n':
    B=a[a['sign']=='n ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='o':
    B=a[a['sign']=='o ']
    a1=B['P1_1'] 
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='p':
    B=a[a['sign']=='p ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='r':
    B=a[a['sign']=='r ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='s':
    B=a[a['sign']=='s ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='t':
    B=a[a['sign']=='t ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='u':
    B=a[a['sign']=='u ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='w':
    B=a[a['sign']=='w ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)
elif wycinanie=='y':
    B=a[a['sign']=='y ']
    a1=B['P1_1']
    a1=a1.head(n=75)  
    a1=abs(np.diff(a1))
    V= [a1[i + 1] + a1[i] for i in range(len(a1)-1)]
    k=sum(V)
    wartosci_GPS= [V/k]
    print(wartosci_GPS)


# In[ ]:

wartosci_GPS = wartosci_GPS[0]
plt.plot(wartosci_GPS)


# In[ ]:




