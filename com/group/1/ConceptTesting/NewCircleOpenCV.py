import cv2
import numpy as np
running = True

cam = cv2.VideoCapture(0)

while running:

 running, frame = cam.read()
img = cv2.medianBlur(frame,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    break

cv2.imshow('detected circles',cimg)
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
