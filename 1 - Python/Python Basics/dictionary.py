# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:38:29 2023

@author: Bedirhan
"""

# %%
#dictionary



dictionary1 = {"ali":21,
              "veli":31,
              "ufuk":11}

print(dictionary1)
print(dictionary1["ali"])

#ali,veli,ufuk = keys
#21,31,11 = values

print(dictionary1.keys())
print(dictionary1.values())

def deneme():
    dictionary2 = {"ali":21,
                  "veli":31,
                  "ufuk":11}
    return dictionary2

print(deneme())
print(deneme()["veli"])
    