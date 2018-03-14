import cv2

cam = cv2.VideoCapture(0)
running = True

while running:

    running, raw_image = cam.read()
    cv2.imshow('Original Image', raw_image)


    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
    cv2.imshow('Bilateral', bilateral_filtered_image)


    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    cv2.imshow('Edge', edge_detected_image)


    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
            contour_list.append(contour)

    cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
    cv2.imshow('Objects Detected',raw_image)
    key = cv2.waitKey(1) & 0xFF


cam.release()
cv2.destroyAllWindows()