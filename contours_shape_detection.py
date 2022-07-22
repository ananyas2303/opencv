#CONTOURS AND SHAPE DETECTION
import cv2
import numpy as np
from cv2 import RETR_EXTERNAL


def getContours(img):
    contours,heirarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri=cv2.arcLength(cnt,True)
        #print(peri)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True) #gives corner points
        print(len(approx))
        objCor=len(approx)
        x,y,w,h=cv2.boundingRect(approx)

        if objCor==3:
            objectType="Triangle"
        elif objCor==4:
            aspRatio=w/float(h)
            if aspRatio>0.95 and aspRatio<1.05:
                objectType="Square"
            else:
                objectType="Rectangle"
        elif objCor==5:
            objectType="Pentagon"
        elif objCor==6:
            objectType="Hexagon"
        elif objCor>10:
            objectType="Circle"
        else:
            objectType="None"

        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(imgContour,objectType,(x+(w//2)-30,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

path="Resources/pic.png"
img=cv2.imread(path)
imgContour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank=np.zeros_like(img)

cv2.imshow("Contour Image",imgContour)

"""
cv2.imshow("Image",img)
cv2.imshow("Grayscale image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Blank image",imgBlank)
"""
cv2.waitKey(0)