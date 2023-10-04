# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:59:45 2023

@author: Bedirhan
"""

#%%
#convert and copy
import numpy as np

liste = [1,2,3,4]

array2 = np.array([5,6,7,8])
#listeden array yapma
array1 = np.array(liste)
print(array1)
print(array2)
print()

#arrayden list yapma
liste2 = list(array2)
print(liste2)
print()

a = np.array([1,2,3,4])
b=a
c=a
#b ve c aynı adresi point ederken d farklı bir alana kopyalandı
d=a.copy()

print("bir arrayde değişiklik yapmak;")
print(a)
print("b için :2 >>> 5")
print()
#a,b ve c aynı adresi point ettiği için hepsinde bu değer değişirken
#d değişkeni farklı bir adresi kopyaladığı için onda değişiklik olmayacaktır
b[1] = 5;



print("a :",a)
print("b :",b)
print("c :",c)
print("d :",d)