#Write a program to take a user defined text input and detect the respective shape in shapes.jpg 
import cv2
import numpy as np
from cv2 import RETR_EXTERNAL

#shape=input("Enter the shape you want to detect: ")
def getContours(img):
    contours,heirarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>250:
            peri=cv2.arcLength(cnt,True) #finds out the perimeter of the shape
            approx=cv2.approxPolyDP(cnt,0.01*peri,True) 
            objCor=len(approx) 
            x,y,w,h=cv2.boundingRect(approx)
            aspRatio=w/float(h)
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),2)

            #Condition for triangle
            if objCor==3:
                objectType="Triangle"
            
            #Condition for shapes with 4 sides
            elif objCor==4:
                if aspRatio>0.85 and aspRatio<1.15:
                    objectType="square"
                    exit
                else:
                    objectType="Rectangle"
            

            #5 sided shape
            elif objCor==5:
                    objectType="Pentagon"
            

            #6 sided shape
            elif objCor==6:
                objectType="Hexagon"

            #7 sided shape
            elif objCor==7:
                    objectType="Heptagon"

            elif objCor==10:
                objectType="Star"

            elif objCor==12:
                objectType="Cross"
            
            elif objCor>25:
                objectType="Circle"

            else:
                objectType="None"
    
    
            #cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            #To put text in shapes
            cv2.putText(imgContour,objectType,(x+(w//2)-20,y+(h//2)+2),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        else:
            pass
path="Resources/shapes2.png"
img=cv2.imread(path)
imgContour=img.copy()
#Converting image to grayscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
num, imgThresh = cv2.threshold(imgGray, 245, 255, cv2.THRESH_BINARY_INV)
getContours(imgThresh)


cv2.imshow("Contour Image",imgContour)
cv2.waitKey(0)
