# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:20:41 2023

@author: Bedirhan
"""

#%%
#list

liste1 = [1,2,3,4,5,6]
print(liste1)

listeStr = ["pzt","sali","crsmb"]
print(listeStr)

#indexler 0'dan başlar
print(liste1[0])
#negatif indexler tersten baslar
print(liste1[-1])


#bir listenin belirli bir parçasını almak için aralık belirtilir;
liste2 = liste1[1:4]
# [a:b] bu aralık; a indexli elemanı içine alırken b indexli elemanı almaz
print(liste2)


# dir() metodu ile list ile kullanılabilecek metodları yazdırır
print(dir(liste1))


#help() metodu ile parametre olarak belirteceginiz metodun görevi öğrenilir
print(help(list.append))

liste1.append(7)
print(liste1)


# en sık kullanılar metodlar

# 'append'
# 'clear'
# 'copy'
# 'count'
# 'extend'
# 'index'
# 'insert'
# 'pop'
# 'remove'
# 'reverse' 
# 'sort'
