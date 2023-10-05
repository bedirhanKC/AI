# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:10:34 2023

@author: Bedirhan
"""

#%%
#indexing and slicing data frames

import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}

dataFrame1 = pd.DataFrame(dictionary)


print(dataFrame1["NAME"])
print()
#bu iki şekilde de kullanılabilir
print(dataFrame1["AGE"])
print(dataFrame1.AGE)
print()

#bu şekilde yeni column ekleyebiliriz
dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]


#bir konumu yazdırmak için matrixler için kullandığımız 
#satır ve sütun bulmayı kullanabiliriz. Örneğin maaş için;

print(dataFrame1.loc[:,"MAAS"])
print()

#sadece bir kısmını yazdırması için de ayarlayabiliriz
#numpy'nin aksine pandas'da duracağı indexi de kapsar
#örneğin bu çıktıda olacağı gibi 0:3 durumunda 3. indexi de yazdırır
print(dataFrame1.loc[0:3,"NAME"])
print()

#bir sütun aralığını da yazdırabiliriz
print(dataFrame1.loc[:3,"NAME":"MAAS"])
print()

#aralık belirlemek dışında sadece istenilen sütunlar da seçilebilir
print(dataFrame1.loc[:3,["NAME","MAAS"]])
print()

#tersten yazdırma indexe göre tersini yazdırır
print(dataFrame1.loc[::-1,:])
print()

#virgülden önceki iki nokta tüm satırları al anlamına gelir
#virgülden sonraki iki noktanın yanında bir giriş varsa, aralık belirler
#örneğin bu satırda AGE'e kadar olan satırları yazdır anlamına gelir
print(dataFrame1.loc[:,:"AGE"])
print()

#sadece column'un ismi ile değil, "iloc" kullanarak indexi ile de çağırabiliriz
#fakat index ile aralık belirlerken son deger exclusive'dir
print(dataFrame1.iloc[:,:2])
print()

print(dataFrame1.iloc[:,2])

























