# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:40:09 2023

@author: Bedirhan
"""

#%%
#shape manipulation
import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array1)
print("-----------")
#bu metod arrayi matrix olmaktan çıkaratarak vektör haline getirir
array2 = array1.ravel()
print(array2)
print("-----------")

#bu method ile vektörü matrix haline getirebiliriz
array2 = array2.reshape(3,3)
print(array2)
print("-----------")

#bu method ile matrixin transpozunu alırız
array2 = array2.T 
print(array2)
print("-----------")

array3 = np.array([[1,2],[3,4],[5,6]])
print(array3,"\n")

#bu method ile matrixin boyutları değiştirilebilir
array3.reshape(2, 3)
#fakat bu method reshape ettiği matrixi değiştirmez
print(array3 , "\n") 
#resize kullanırsak işlem yaptığımız matrixin boyutlarını kalıcı olarak değiştiririz
array3.resize(2, 3)
print(array3 ) 