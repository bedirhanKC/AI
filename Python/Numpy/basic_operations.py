# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:47:03 2023

@author: Bedirhan
"""

#%%
#numpy basic operations

import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1)
print(array2)
print("--------------")
print("toplama          :",array1+array2)
print("cıkarma          :",array1-array2)
print("array1'in karesi :",array1**2)
print("--------------")
print("array'in sinüsü :",np.sin(array1))
print(array1 < 2)
print("--------------")
array3 = np.array([[1,2,3],[4,5,6]])
array4 = np.array([[1,2,3],[4,5,6]])
print(array3,"\n")
print(array4)
print("--------------")
#element wise product (aynı indexleri birbiriyle çarpma)
print("element wise product;")
print(array3*array4,"\n")
#matrix product (klasik matrix çarpımı)
#print(array3.dot(array4)) 
#bu kod çalışmaz çünkü 3'ün sütun sayısı ile 4'ün satır sayısı aynı olmalı
print("matrix product;")
array4 = array4.T #bu yüzden 4'ün transpozunu alırsak 2ye 3lük değil 3e 2lik bir matrix olur
print(array3.dot(array4),"\n")

print("üstel hesaplama;")
print(np.exp(array3),"\n")

array5 = np.random.random((4,4))
print("random matrix;")
print(array5)

