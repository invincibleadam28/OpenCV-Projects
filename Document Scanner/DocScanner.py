import cv2
import numpy as np

widthImg=640
heightImg=480

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,200,200)
    kernel= np.ones((5,5))
    imgDila= cv2.dilate(imgCanny,kernel,iterations=2)
    imgThresh= cv2.erode(imgDila,kernel,iterations=1)

    return imgThresh

def reorder(myPoints):
    myPoints=myPoints.reshape((4,2))

def getWarp(img,biggest):
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut= cv2.warpPerspective(img, matrix, (widthImg,heightImg))

    return imgOut

def getContours(img):
    biggest= np.array([])
    maxArea=0

    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        #cv2.drawContours(imgCont,cnt,-1,(0,0,255),3)
        if area>5000:
            peri= cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)

            if area> maxArea and len(approx) == 4:
                biggest=approx
                maxArea=area
    cv2.drawContours(imgCont, biggest, -1, (0, 0, 255), 20)
    return biggest

while True:
    success, img=cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgCont = img.copy()
    imgThresh= preProcessing(img)
    biggest= getContours(imgThresh)

    imageWarped= getWarp(img, biggest)
    cv2.imshow("Video",imageWarped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
