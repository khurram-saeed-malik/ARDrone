
from time import sleep

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
running = True


while running:
    # get current frame of video
    running, frame = cam.read()
    status = "No Targets"

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    kernel = np.ones((2, 3), np.uint8)
    hsv = cv2.erode(hsv, kernel, iterations=1)

    hsv = cv2.dilate(hsv, kernel, iterations=1)

    # define range of blue color in HSV
    lower_blue = np.array([0, 50, 60])
    upper_blue = np.array([15, 150, 180])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # detect circles in the image
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 260, param1=30, param2=65, minRadius=0, maxRadius=10)
    # print circles

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(mask, (x, y), r, (20, 85, 30), 4)
            cv2.rectangle(mask, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # time.sleep(0.5)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()











