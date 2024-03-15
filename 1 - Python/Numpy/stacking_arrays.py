# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:54:48 2023

@author: Bedirhan
"""

#%%
#stacking arrays
import numpy as np

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
print(array1)
print()
print(array2)
print()


#vertical(dikey) birleştirme
array3 = np.vstack((array1,array2))
print("Vertical;")
print(array3)
print()

#horizontal(yatay) birlestirme
array4 = np.hstack((array1,array2))
print("horizontal;")
print(array4)