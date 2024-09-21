# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2
import matplotlib.pyplot as plt

# image thresholding: convering color image to binary
img = cv2.imread("img1.jpg")
img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orjinal Resim")

# eşik değeri belirle
"""
Parametreler
      src girdi dizisi (çok kanallı, 8 bit veya 32 bit kayan nokta).
      dst çıktı dizisi aynı boyut ve tipte ve src ile aynı sayıda kanala sahip.
      eşik değeri.
      THRESH_BINARY ve THRESH_BINARY_INV eşik türleriyle kullanılacak maksimum maksimum değer.
      tür eşikleme türü (bkz. ThresholdTypes).
"""
# threshold değeri üzerindekileri beyaz yap altındakileri siyah yap
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.title("Threshold")
"""
Parametreler
    src Kaynak 8 bitlik tek kanallı görüntü.
    dst Aynı boyutta ve src ile aynı tipte hedef görüntüsü.
    maxValue Koşulun karşılandığı piksellere atanan sıfır olmayan değer
    adaptiveMethod Kullanılacak uyarlanabilir eşikleme algoritması, bkz. AdaptiveThresholdTypes. BORDER_REPLICATE | BORDER_ISOLATED, sınırları işlemek için kullanılır.
    THRESH_BINARY veya THRESH_BINARY_INV olması gereken eşik türü Eşikleme türü, bkz. Eşik Türleri.
    blockSize Piksel için bir eşik değeri hesaplamak için kullanılan bir piksel mahallesinin boyutu: 3, 5, 7, vb.
    C Sabit, ortalamadan veya ağırlıklı ortalamadan çıkarılır (aşağıdaki ayrıntılara bakın). Normalde pozitiftir ancak sıfır veya negatif de olabilir.
"""
"""
Önceki bölümde eşik değer olarak global bir değer kullandık. 
Ancak görüntünün farklı alanlarda farklı aydınlatma koşullarına sahip olduğu tüm koşullarda iyi olmayabilir.
Bu durumda, uyarlamalı eşiklemeye gidiyoruz. 
Bunda, algoritma görüntünün küçük bir bölgesi için eşiği hesaplar. 
böylece aynı görüntünün farklı bölgeleri için farklı eşikler elde ederiz ve 
bu bize farklı aydınlatmaya sahip görüntüler için daha iyi sonuçlar verir.
"""
# cv2.ADAPTIVE_THRESH_MEAN_C: eşik değeri, mahalle alanının ortalamasıdır.
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.title("Adaptive Threshold")















