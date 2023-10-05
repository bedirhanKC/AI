# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:00:41 2023

@author: Bedirhan
"""

#%%
#list comprehension
import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1)
print()

#mean() methodu ortalama hesabı yapar
ortalamaMaas = dataFrame1.MAAS.mean()
print("ortalama maas pandas :",ortalamaMaas)

import numpy as np

#aynı şekilde mean methodu numpy kütüphanesinde de bulunmaktadır
ortamaMaasNp = np.mean(dataFrame1.MAAS)
print("ortalama maas numpy :",ortamaMaasNp)
print()

#bu satır yeni bir column oluşturur
#data frame'in tüm maaşlarını for each ile dolaşır
#her dolaştığı satırda maaşın ortalama maaş ile olan durumuna bakar
#yeni oluşturulmuş sütuna eğer maaş ortalama maaştan küçükse "düşük" değilse "yüksek" yazar
dataFrame1["MAAS_SEVIYESI"] = ["dusuk" if ortalamaMaas > each else "yuksek" for each in dataFrame1.MAAS]

#bu satır olan columnları değiştirir
#tüm columları for each ile dolaşır
#aldığı each değerini lower case yaparak tekrar yazar
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

#bu satır olan columnları değiştirmek için kullanılır
#tüm columnlar yine for each ile dolaşılır
#alınan each değerine split() methodu uygulanır
#split methodu eğer boşluk varsa ayrı olan iki kelimeyi iki farklı değişken yapar
#burdaki kontrol yapımız each.splitin uzunluğunun 1'den büyük olup olmadığını kontrol eder
#eğer büyükse boşluklu bir yazım olduğu anlaşılır
#if öncesi kısımda ise ayrılan iki kelime alttan çizgi ile birleştirilir
#eğer if sağlanmazsa columndaki each değerini olduğu gibi tekrar yazar
dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]





















