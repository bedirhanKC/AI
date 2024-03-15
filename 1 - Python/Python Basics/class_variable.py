# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:55:10 2023

@author: Bedirhan
"""

#%%
#class variable

class Calisan:
    
    email = "undefined"
    zamOrani = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@dotgamestudios.com"
    
        Calisan.counter += 1
    
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim

    def zamYap(self):
        self.maas += self.maas*self.zamOrani

calisan1 = Calisan("bedirhan", "kömürcü", 3200)
calisan2 = Calisan("ali", "şan", 2200)
calisan3 = Calisan("veli", "ak", 1900)
print(calisan1.giveNameSurname(),"ilk maas :",calisan1.maas)
calisan1.zamYap()
print(calisan1.giveNameSurname(),"yeni maas :",calisan1.maas)
print("toplam calisan sayisi :",calisan1.counter)
