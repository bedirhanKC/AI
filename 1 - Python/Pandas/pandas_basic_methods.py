# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:01:59 2023

@author: Bedirhan
"""

#%%
# Pandas basic methods
import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}

dataFrame1 = pd.DataFrame(dictionary)

#bu method data framin sütunlarını verir
print(dataFrame1.columns)
print()

#data frame hakkında genel bilgi verir
print(dataFrame1.info())
print()

#data framedeki columların tipini verir
print(dataFrame1.dtypes)
print()

#bu method ise sadece numeric featureları alır
print(dataFrame1.describe())
print()

