# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2
import numpy as np

img = cv2.imread("warpPerspectiveImage.png")
cv2.imshow("img", img)

width = 400
height = 500

# şeklimizin köşeleri (pointleri) belirleniyor.
pts1 = np.float32([[203,1],
                   [1,472],
                   [540,150],
                   [338,617]])

pts2 = np.float32([[0,0],
                   [0,height],
                   [width,0],
                   [width,height]])


matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

#dönüştürülmüş görsel
editedImage = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("warped img", editedImage)