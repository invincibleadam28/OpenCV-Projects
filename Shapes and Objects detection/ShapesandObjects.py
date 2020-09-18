import cv2
import numpy as np

path = "Resources/Shapes2.png"
img = cv2.imread(path)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny= cv2.Canny(imgBlur,50,50)
imgContour= img.copy()
def getContours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        #print(area)
        cv2.drawContours(imgContour,cnt,-1,(0,0,255),3)
        if area>500:
            peri= cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            if objCor == 3: ObjectType= "Triangle"
            elif objCor== 4 : ObjectType= " Rectangle"
            elif objCor == 6:
                ObjectType = "Hexagon"
            elif objCor == 5:
                ObjectType = "Pentagon"
            else: ObjectType= "Circle"

            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,0))
            cv2.putText(imgContour,ObjectType,(x+w//2-10,y+h//2-10),cv2.FONT_ITALIC,0.5,(0,0,255),2)


getContours(imgCanny)
#cv2.imshow("Original",img)
#cv2.imshow("Blurred",imgBlur)
cv2.imshow("Canny Edge",imgCanny)
cv2.imshow("Contours",imgContour)

cv2.waitKey(0)