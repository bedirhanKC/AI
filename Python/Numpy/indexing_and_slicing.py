# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:28:49 2023

@author: Bedirhan
"""

#%%
#indexing and slicing

import numpy as np

array1 = np.array([1,2,3,4,5,6,7])
print(array1)

reverseArray1 = array1[::-1]
print(reverseArray1)

print("-----------")

array2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2)
print(array2[1,2])
print("-----------")

# : işareti hepsi anlamına gelir
print(array2[:,1])
# 1:4  1numaralık indeks ile 4 numaralı indeks arasındaki elemanları seçer(4 dahil değil)
print(array2[1,1:4])
# son sırayı (sütün ya da satırı) kullanmak için -1 kullanılır
print(array2[-1,])
print(array2[:,-1])