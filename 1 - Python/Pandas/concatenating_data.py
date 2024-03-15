# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:23:06 2023

@author: Bedirhan
"""

#%%
#drop and concatenating

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



#drop

#drop bir grubu droplamaya yarar
#ilk parametre droplanacak yeri belirler
#ikinci parametre, axis 1, sütunun droplanacağını belirler
#eğer axis 0 olsaydı satır droplanırdı
#inplace de droplanılan yeni sütunu dataFrame1'de de droplanır
#eğer false olsaydı dataFrame1 değişmeyecekti
dataFrame1.drop(["yeni_feature"],axis = 1, inplace = True)


#concatenating

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
data_concat = pd.concat([data1,data2],axis=0)

#horizonttal
maas = dataFrame1.maas
age = dataFrame1.age

dataHConcat = pd.concat([maas,age],axis=1)






