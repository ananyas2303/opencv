#BASIC FUNCTIONS
import cv2
import numpy as np

img=cv2.imread("Resources/pic.png")
kernel=np.ones((5,5),np.uint8) #defining a kernel
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #for making image grayscale
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0) #for blurring the image
imgCanny=cv2.Canny(img,50,20) #for edge detection
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1) #for dilating images
imgErode=cv2.erode(imgDilation,kernel,iterations=1) #for erosion of image i.e. opposite of dilation
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilaton Image",imgDilation)
cv2.imshow("Eroded Image",imgErode)
cv2.waitKey(0)