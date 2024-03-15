# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:18:19 2023

@author: Bedirhan
"""

#%%
#video quiz 1
# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float()) 
# *args soyisim
# default parametre ayakkabi numarasi
    
yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi: ",name, " yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)



#%%
#video quiz 2
#yüzyıl bulma


def yuzyil(yil):
    """

    Parameters
    ----------
    yil : int
        yuzyila dönecek yıl.

    Returns
    -------
    int
        yüzyıl.

    """
    yuzyil = yil/100
    
    if(yuzyil>int(yuzyil)):
        yuzyil = int(yuzyil)+1
        
    return int(yuzyil)

print(yuzyil(1001))



#%%
#video quiz 3
#parametresi liste olan func ile listenin en kucuk sayisini bulma


def findMin(liste):
    """

    Parameters
    ----------
    liste : liste
        normal bir liste.

    Returns
    -------
    min : int
        listenin min degeri

    """
    
    mini = liste[0]
    for each in liste:
        if(mini>each):
            mini = each
    
    return mini

liste=[11,17,6,27,3,-11,22]

print(findMin(liste))



