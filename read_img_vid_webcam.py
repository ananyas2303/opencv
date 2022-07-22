#READING IMAGE,VIDEO,WEBCAM
import cv2
print('Package Imported') 

#for image
"""img=cv2.imread("Resources/pic.png")
cv2.imshow("Output",img)
cv2.waitKey(0) """

#for video files 
"""cap=cv2.VideoCapture(file name)
while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF=="ord('q'):
        break

"""

#for webcam
"""cap=cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #brightness
while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
"""


