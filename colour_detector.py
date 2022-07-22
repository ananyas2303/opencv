#COLOUR DETECTOR
import cv2
import numpy as np

def empty(a):
    pass

img=cv2.imread("Resources/pic.png")
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",650,250) #To create a window for trackbar
cv2.createTrackbar("Hue min","Trackbars",0,179,empty) #Creating a trackbar for min and max hue
cv2.createTrackbar("Hue max","Trackbars",179,179,empty) 
cv2.createTrackbar("Sat min","Trackbars",0,255,empty) 
cv2.createTrackbar("Sat max","Trackbars",255,255,empty) 
cv2.createTrackbar("Val min","Trackbars",0,255,empty) 
cv2.createTrackbar("Val max","Trackbars",255,255,empty) 
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #to create an HSV image
cv2.imshow("Original Image",img)
cv2.imshow("HSV Image",imgHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()