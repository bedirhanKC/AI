# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:45:22 2023

@author: Bedirhan
"""

#%%
# 1- Pandas dataframeler için hızlı ve etkili
# 2- csv ve text dosyalarını açıp inceleyip sonuçlarımızı bu dosya tiplerine 
# rahat bir şekilde kaydedebiliriz
# 3- missing data'lar için işimizi kolaylaştırır
# 4- reshape yaparak datayı daha etkili bir şekilde kullanabiliriz
# 5- Kolay slicing ve indexing kullanımı
# 6- time series data analizinde çok yardımcı olur
# 7- en önemlisi hız ve pandas hız açısından optimize edilmiş hızlı bir kütüphane

import pandas as pd

dictionary = {"NAME":["ali","veli","şenay","ufuk","ayse","bedirhan"],
              "AGE":[15,16,21,32,45,21],
              "MAAS":[100,150,360,210,140,230]}


#bu şekilde oluşturduğumuz dictionaryi data frame yapabiliriz
dataFrame1 = pd.DataFrame(dictionary)

#bu metod ile data frame içindeki ilk 5 satırı alır
head= dataFrame1.head()
#bu metod ile data frame içindeki son 5 satırı alır
tail = dataFrame1.tail()

#ayrıca bu metodlara parametre olarak eklenecek deger;
#data frameden kaç satır gösterileceğini belirler.
# örneğin : dataFrame1.head(50), ilk 50 satırı gösterir