# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:19:23 2023

@author: Bedirhan
"""

#%%
#numpy kütüphanesi
#sum(),int(),print()


#numpy'ı import edip, kısayol olarak np atama işlemi
import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1e 15 lik vector
print(array1)
print(array1.shape)

print("\n")

a = array1.reshape(3, 5)
print(a)
#matrixi kaça kaç olduğunu gösterir
print("shape     :",a.shape)
#matrixin boyutunu gösterir
print("dimension :",a.ndim)
#matrixin içindeki dataların tipini gösterir
print("data type :",a.dtype.name)
#matrixin boyutunu verir
print("size      :",a.size)
print("type :",type(a))

print("\nArray 2\n")

array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)
print("shape     :",array2.shape)
print("dimension :",array2.ndim)
print("data type :",array2.dtype.name)
print("size      :",array2.size)
print("type :",type(array2))

print("\nZeros-Array 3\n")

#bu metod girilen satır ve sutun oranıyla 0'lardan oluşturulmuş matrix verir
array3 = np.zeros((3,4))
print(array3)

print("\n")

array3[0,0] = 12
print(array3)

print("\nOnes-Array 4\n")
array4 = np.ones((3,3))
print(array4)


print("\nEmpty-Array 5\n")
array5 = np.empty((2,3))
print(array5)

print("\narange - Array 6\n")
#10 ile 50 arasındaki sayıları 5er 5er yazdirma;
array6 = np.arange(10,50,5)
print(array6)

print("\nlinescpae - Array 7\n")
#10 ile 50 arasından 5 tane sayıyı yazdirma;
array7 = np.linspace(10, 50,5)
print(array7)



