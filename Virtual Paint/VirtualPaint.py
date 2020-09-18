import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

myColors=[[164,120,0,179,251,255]]
myPoints=[]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,(0,0,255),cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y])
        #cv2.imshow("img",mask)
    return newPoints

def getContours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h =0,0,0,0
    for cnt in contours:
        area= cv2.contourArea(cnt)
        #cv2.drawContours(imgResult,cnt,-1,(0,0,255),3)
        if area>500:
            peri= cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints):
    for points in myPoints:
        cv2.circle(imgResult, (points[0], points[1]), 10, (0, 0, 255), cv2.FILLED)

while True:
    success, img=cap.read()
    imgResult=img.copy()
    newPoints= findColor(img, myColors)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints)
    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
