#SHAPES AND TEXT
import cv2
import numpy as np
img=np.zeros((500,500,3),np.uint8)

"""
print(img)
img[200:300,100:300]=255,0,0 #to change the colour of the specified dimensions
"""

#cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) #To fill the rectangle use cv2.FILLLED instead of thickness parameter
cv2.circle(img,(400,50),30,(255,0,0),5)
cv2.putText(img,"nigga",(300,200),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,150,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)