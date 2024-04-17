# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:16:40 2023

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime as dt
import time

gesty = pd.read_csv(r'C:\Users\kacpo\Desktop\gesty.csv')
przedzial_czasowy = gesty['timestamp']
Przedzial_czasowy = pd.to_datetime(przedzial_czasowy)
PRZEDZIAL_CZASOWY = Przedzial_czasowy.dt.second
PRZEDZIAL_CZASOWY_1 = Przedzial_czasowy.dt.microsecond
a = Przedzial_czasowy
b = PRZEDZIAL_CZASOWY * 0.001
c = PRZEDZIAL_CZASOWY
d = PRZEDZIAL_CZASOWY_1/ 1000000
e = c + d
print("cały timestamp:")
print(a)
print("Sekundy:")
print(c)      
print("Microsekundy:")
print(d)
print("Sekundy z mikrosekundami:")
print(e)
      
#Ogarnąć czas na milisekundy i wtedy dodać do algorytmu
