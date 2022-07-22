#JOINING IMAGES(both images need to be of the same type, i.e either rgb or grayscale)
import cv2
import numpy as np

img=cv2.imread("Resources/pic.png")
imgHor=np.hstack((img,img)) #to stack two images horizontally, i.e attach them side by side
imgVer=np.vstack((img,img)) #to stack two images vertically, i.e attach them on top and bottom
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)