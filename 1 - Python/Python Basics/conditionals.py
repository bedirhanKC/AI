# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:07:59 2023

@author: Bedirhan
"""

#%%
#Conditionals

#if else

var1 = 30
var2 = 20

if(var1>var2):
    print("var1 > var2")
    
elif(var1==var2):
    print("var1 = var2")
else:
    print("var1 < var2")
    
    
liste = [1,2,3,4,5]


value = 3
if value in liste:
    print("{} listede".format(value))
else:
    print("{} listede degil".format(value))
    
    
dictionary1 = {"ali":21,
              "veli":31,
              "ufuk":11}


keys = dictionary1.keys()

if "mahmut" in keys:
    print("true")
else:
    print("false")
    

# %%
#Loop

#for loop

for each in range(1,11):
    print(each)

print("\n")

for each in "ankara konya":
    print(each)
    
print("\n")
    
#split() metodunun default degeri kelimeleri boşluklarına göre ayırır
for each in "ankara konya".split():
    print(each)
    

print("\n")

#liste toplamı bulma
liste = [1,6,12,3,6,9,41]
toplam1 = sum(liste)

toplam2 = 0
for each in liste:
    toplam2 += each

print("toplam1 :",toplam1)
print("toplam2 :",toplam2)

print("\n\nwhile loop\n")
    
#while loop

i=0
while(i<5):
    print(i)
    i+=1
    

print("\n")

sinir = len(liste)
each = 0
count = 0

while(each<sinir):
    count += liste[each]
    each+=1
    
print("liste toplam :",count)









    