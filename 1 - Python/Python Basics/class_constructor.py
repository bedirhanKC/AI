# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:45:44 2023

@author: Bedirhan
"""

#%%
#class constructor

class Calisan:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@dotgamestudios.com"
    
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
    

isci1 = Calisan("bedirhan", "komurcu", 3000)
isci2 = Calisan("ali", "karan", 2000)
isci3 = Calisan("veli", "ak", 2500)
print(isci1.giveNameSurname())

