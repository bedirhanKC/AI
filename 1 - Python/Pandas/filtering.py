# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:33:35 2023

@author: Bedirhan
"""

#%%
# Filtering Pandas Data Frame
import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}

dataFrame1 = pd.DataFrame(dictionary)


#öncelikle bir filtre oluşturuyoruz. bu durumeda maaş'ın 200'den yüksek olması
filtre1 = dataFrame1.MAAS > 200

#filtrelenmis dataları oluşturduğumuz yeni değişkende tutuyoruz
filtrelenmisData1 = dataFrame1[filtre1]
print(filtrelenmisData1)
print()

filtre2 = dataFrame1.AGE < 25

#bu şekilde aynı anda birden fazla filtre uygulayabiliriz
filtrelenmisData2 = dataFrame1[filtre1 & filtre2]
print(filtrelenmisData2)
print()

#yeni bir değişken oluşturmadan filtreyi kapalı parantez içinde de kullanabiliriz
print(dataFrame1[dataFrame1.AGE > 30])


















