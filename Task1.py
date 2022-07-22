#Write a program to take a user defined text input and detect the respective shape in shapes.jpg 
import cv2
import numpy as np
from cv2 import RETR_EXTERNAL

shape=input("Enter the shape you want to detect: ")
def getContours(img):
    contours,heirarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri=cv2.arcLength(cnt,True)
        #print(peri)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True) #gives corner points
        #print(len(approx))
        objCor=len(approx)
        x,y,w,h=cv2.boundingRect(approx)

        #Condition for triangle
        if objCor==3:
            objectType="Triangle"
        
        #Condition for shapes with 4 sides
        elif objCor==4:
            aspRatio=w/float(h)
            if aspRatio>0.95 and aspRatio<1.05:
                objectType="square"
            else:
                objectType="rectangle"
            

        #5 sided shape
        elif objCor==5:
            objectType="pentagon"
            

        #6 sided shape
        elif objCor==6:
            objectType="hexagon"
            

        #Condition for circle
        elif objCor>10:
            objectType="circle"
            
        else:
            objectType="none"

        #cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        #To put text in shapes
        cv2.putText(imgContour,objectType,(x+(w//2)-30,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

path="Resources/shapes.png"
img=cv2.imread(path)
imgContour=img.copy()
#Converting image to grayscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blurring the image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow("Contour Image",imgContour)
cv2.waitKey(0)
