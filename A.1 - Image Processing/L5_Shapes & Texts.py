# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2
import numpy as np

# shape and text
img = np.zeros((512,512,3),np.uint8) # siyah bir resim oluştur
print(img.shape)
cv2.imshow("Image", img)

cv2.line(img,(0,0),(512,512), (0,255,0), 2) # start - stop - color - thickness
cv2.imshow("Image", img)

cv2.rectangle(img,(0,0),(256,256), (255,0,0), cv2.FILLED) # (bgr)
cv2.imshow("Image", img)

cv2.circle(img,(300,300),30, (0,0,255)) # center - radius
cv2.imshow("Image", img)

cv2.putText(img,"CIRCLE ",(325,305),cv2.FONT_HERSHEY_COMPLEX, 1 ,(255,0,255))
cv2.imshow("Image", img)
