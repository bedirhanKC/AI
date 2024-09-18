# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2

img= cv2.imread("resizeAndCropImageImage.jpg",0)
print("image size : ", img.shape)
cv2.imshow("main img",img)

imgResized = cv2.resize(img, (800,600))
print("resized image size : ", imgResized.shape)
cv2.imshow("resized img",imgResized)
cv2.imwrite('resizeAndCropImageResizedImage.jpg', imgResized)

imgCropped = imgResized[:500,250:750]
cv2.imshow("cropped img",imgCropped) 
cv2.imwrite('resizeAndCropImageCroppedImage.jpg', imgCropped)