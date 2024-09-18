# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2

# içe aktarma
img = cv2.imread("importImagePhoto.jpg",0)

# görselleştirme
cv2.imshow("First Image",img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('importImagePhotoNewVersion.jpg', img)
    cv2.destroyAllWindows()