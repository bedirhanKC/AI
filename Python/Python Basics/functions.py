# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:22:48 2023

@author: Bedirhan
"""

#Functions

#%%
#built in functions

str1 = "deneme"
uzunluk = len(str1)
print(uzunluk)

float1 = 10.4
print(round(float1))
#bu fonksiyon ondaliklik sayiyi yakin oldugu tam sayiya yuvarlar

# %%
#User Defined Functions

var1 = 10
var2 = 100

def func(var1,var2):
    """
    denklemin sonucunu hesaplar
    """
    return (((var1+var2)*50)/100.0)*(var2/var1)


output1 = (((var1+var2)*50)/100.0)*(var2/var1)
output2 = func(var1,var2)
print("output1 :" , output1)
print("output2 :", output2)

#%%
#default & flexible functions

#default
print("default")

#bu fonksiyondaki "pi = 3.14", default deger atamadir
def cemberCevresiHesaplama(r,pi = 3.14):
    """
    Parameters
    ----------
    r : yaricap
    pi :pi sayisi. The default is 3.14.

    Returns
    -------
    cember cevresi
    """
    return 2*pi*r

print(cemberCevresiHesaplama(3))
print(cemberCevresiHesaplama(3,1))
#default olarak ayarlanan parametre icin yeni degerler verilebilir


#flexible
print("\nflexible")

# bu fonksiyonda boy ve kilo kesinlikle olmalıyken, *args ile ekstra parametreler eklenebilir
def hesapla(boy,kilo,*args):
    print(args)

hesapla(5,6)
hesapla(5,6,3,2)

# %%
#lambda functions

def kareal1(x):
    return x*x
print("normal func :",kareal1(3))


kareal2 = lambda x:x*x
print("lambda func : ",kareal2(3))


