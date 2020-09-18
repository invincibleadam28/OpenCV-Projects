import cv2
import numpy as np
path = "Resources/Car.jpg"
imgk = cv2.imread(path)
img = cv2.resize(imgk,(640,480))
def empty(a):
    pass


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",720,320)
cv2.createTrackbar("Hue Min","TrackBar",0, 179,empty)
cv2.createTrackbar("Hue Max","TrackBar",179, 179,empty)
cv2.createTrackbar("Sat Min","TrackBar",62, 255,empty)
cv2.createTrackbar("Sat Max","TrackBar",255, 255,empty)
cv2.createTrackbar("Val Min","TrackBar",25, 255,empty)
cv2.createTrackbar("Val Max","TrackBar",255, 255,empty)


while True:

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min= cv2.getTrackbarPos("Hue Min","TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBar")
    v_min = cv2.getTrackbarPos("Val Min","TrackBar")
    v_max = cv2.getTrackbarPos("Val Max","TrackBar")

    lower= np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask = mask)

    cv2.imshow("Original",img)
    cv2.imshow("Modified",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)


    cv2.waitKey(1)