#RESIZING AND CROPPING
import cv2
import numpy as np

img=cv2.imread("Resources/pic.png")
print(img.shape) #to print the dimensions of an image
imgResize=cv2.resize(img,(300,200)) #(width,height)
print(imgResize.shape)
imgCropped=img[0:200,200:500] #(height,width)
cv2.imshow("Image",img)
cv2.imshow("Resized image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)