# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:38:02 2023

@author: Bedirhan
"""

#%%
#transforming data

import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

ortalamaMaas = dataFrame1.MAAS.mean()
dataFrame1["MAAS_SEVIYESI"] = ["dusuk" if ortalamaMaas > each else "yuksek" for each in dataFrame1.MAAS]
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]
dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]


dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]


#apply() methodu kullanımı

def multiply(age):
     return age*2

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)




