import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

#img[200:300,300:400]= 255,0,0

cv2.line(img,(450,50),(50,450),(130,230,30),4)
cv2.line(img,(450,450),(50,50),(130,230,30),4)
cv2.line(img,(50,450),(450,50),(130,230,30),4)
cv2.line(img,(450,50),(450,450),(130,230,30),4)
cv2.line(img,(50,50),(50,450),(130,230,30),4)
cv2.rectangle(img,(0,200),(100,300),(130,130,250),4)
cv2.circle(img,(250,250),(75),(200,100,65),cv2.FILLED)
cv2.putText(img,"OpenCV",(190,250),cv2.FONT_ITALIC,1,(0,255,200),2)

cv2.imshow("My Image",img)

cv2.waitKey(0)