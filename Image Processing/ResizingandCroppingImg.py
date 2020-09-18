import cv2
import numpy as np

img = cv2.imread("Resources/Rachel.png")
print(img.shape)

imgResize = cv2.resize(img,(640,480))

imgCropped= imgResize[100:360,200:550]

cv2.imshow("Cropped Image", imgCropped)
cv2.imshow("Resized Image",imgResize)
cv2.waitKey(0)


