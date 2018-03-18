from time import sleep

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
running = True

while running:
    # get current frame of video
    running, frame = cam.read()
    status = "No Targets"


    if running:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            # escape key pressed
            running = False
    else:
        # error reading frame
        print 'error reading video feed'

    if not running:
        break

    bilateral_filtered_image = cv2.bilateralFilter(frame, 5, 175, 175)


    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    cv2.imshow('Edge', edge_detected_image)

    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30)):
            contour_list.append(contour)

    cv2.drawContours(edge_detected_image, contour_list, -1, (255, 0, 0), 2)
    cv2.imshow('Objects Detected', frame)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0, 150, 100])
    upper_blue = np.array([15, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # apply GuassianBlur to reduce noise. medianBlur is also added for smoothening, reducing noise.
    gray = edge_detected_image
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.medianBlur(gray, 5)

    # Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, 11, 3.5)

    kernel = np.ones((2, 3), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)

    # gray = erosion

    gray = cv2.dilate(gray, kernel, iterations=1)


        # detect circles in the image
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 260, param1=30, param2=65, minRadius=0, maxRadius=0)
        # print circles

        # ensure at least some circles wedge_detected_imageere found
    if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

            # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle in the image
                # corresponding to the center of the circle
            cv2.circle(edge_detected_image, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(edge_detected_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                # time.sleep(0.5)

            # Display the resulting frame
            cv2.imshow('gray', gray)
            cv2.imshow('res', res)
            cv2.imshow('mask', mask)
            cv2.imshow('woop', edge_detected_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
