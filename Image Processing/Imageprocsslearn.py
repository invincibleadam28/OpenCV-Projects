import cv2
import numpy as np
img = cv2.imread("Resources/Adam.jpg")
kernel = np.ones((5,5),np.uint8)

imgCanny = cv2.Canny(img,100,100)
imageDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imageEroded = cv2.erode(imgCanny,kernel,iterations=1)

cv2.imshow("Canny Img",imgCanny)
cv2.imshow("Dilation Image", imageDilation)
cv2.imshow("Ëroded Image", imageEroded)
cv2.waitKey(0)