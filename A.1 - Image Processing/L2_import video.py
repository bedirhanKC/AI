# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2
import time

videoName = "importVideoVideo.mp4"

# import video
cap = cv2.VideoCapture(videoName)

print("Genişlik : ", cap.get(3))
print("Yükseklik : ", cap.get(4))

# empty video check
if cap.isOpened() == False:
    print("Video içe aktarılamadı.")

while True:
    ret , frame = cap.read()

    if ret == True:
        time.sleep(0.01) # video hızının yavaşlatılması sağlanıyor
        cv2.imshow("Video",frame)
        
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release() #stop capture
cv2.destroyAllWindows()