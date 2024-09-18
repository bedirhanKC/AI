# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2
import numpy as np

# joining images
img = cv2.imread("Lenna_(test_image).png")
cv2.imshow("Orjinal", img)

hor = np.hstack((img,img))
cv2.imshow("Horizontal Image", hor)
 
ver = np.vstack((img,img))
cv2.imshow("Vertical Image", ver)

