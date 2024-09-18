# -*- coding: utf-8 -*-
"""
https://github.com/bedirhanKC
"""

import cv2

#capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

#record video
writer = cv2.VideoWriter("recordVideoVideo.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))
# 1. parametre: "recordVideoVideo.mp4" -> Kayıt edilecek video dosyasının adı.
# 2. parametre: cv2.VideoWriter_fourcc(*"DIVX") -> Kullanılacak video codec formatı.
#    "DIVX" yaygın bir video sıkıştırma formatıdır.
#    Alternatif codec'ler: "XVID", "MJPG", "MP4V" vb.
# 3. parametre: 20 -> FPS (Saniyede çekilecek kare sayısı). Burada 20 FPS belirlenmiş.
# 4. parametre: (width, height) -> Videonun çözünürlüğü (genişlik, yükseklik).

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()


