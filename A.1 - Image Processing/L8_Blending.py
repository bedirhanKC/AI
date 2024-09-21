# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
""" 

import cv2
import matplotlib.pyplot as plt

# blending
img1 = cv2.imread("img1.jpg")
img1= cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#show imgs
plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

#show img sizes
print(img1.shape)
print(img2.shape)


print("")
#img resize
img1 = cv2.resize(img1,(600,600))
print(img1.shape)
img2 = cv2.resize(img2,(600,600))
print(img1.shape)

#show imgs w/ new sizes
plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

# blended = alpha*img1 + beta*img2 + gamma
blended = cv2.addWeighted(src1=img1, alpha = 0.3, src2=img2,beta=0.7, gamma = 0)
plt.figure()
plt.imshow(blended)