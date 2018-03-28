# coding=utf-8
from time import sleep
from lib import libardrone
import QRReader
import cv2

drone = libardrone.ARDrone()


def detect(cam):
    # qr_reader = QRReader
    running = True

    drone.takeoff()
    sleep(3)

    while running:
        # get current frame of video
        running, frame = cam.read()
        status = "No Targets"
        qr_status = "No QR"

        if running:

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # when 'q' key pressed
                print("landing")
                drone.land()
                sleep(3)
                running = False
        else:
            # error reading frame
            print 'error reading video feed'

        if not running:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite("pic1_grascayle.png", gray)
        # Hvad bruger vi dem til?:
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        # cv2.imwrite("pic2_blurred.png", blurred)
        edged = cv2.Canny(blurred, 50, 150)
        # cv2.imwrite("pic3_edged.png", edged)
        # print 'DONE TAKING IMAGES'

        # Hvad finder den helt præcist?
        (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # loop over the contours , Hvordan skal den forstås?
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True)

            # ensure that the approximated contour is "roughly" rectangular
            if 4 <= len(approx) <= 6:
                # compute the bounding box of the approximated contour and
                # use the bounding box to compute the aspect ratio
                (x, y, w, h) = cv2.boundingRect(approx)
                aspectRatio = w / float(h)

                # compute the solidity of the original contour
                area = cv2.contourArea(c)
                hullArea = cv2.contourArea(cv2.convexHull(c))
                solidity = area / float(hullArea)

                # compute whether or not the width and height, solidity, and
                # aspect ratio of the contour falls within appropriate bounds
                keepDims = w > 25 and h > 25
                keepSolidity = solidity > 0.9
                keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.2

                # ensure that the contour passes all our tests
                if keepDims and keepSolidity and keepAspectRatio:
                    # draw an outline around the target and update the status
                    # text
                    cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
                    status = "Found square(s)"

                    print(x, y, w, h)


                    if w > 85:

                        drone.land()

                    else:
                        drone.move_forward()
                        sleep(1)
                        drone.hover()
                        sleep(5)

                    # detect qr
                    # qr_reader.read(gray)

                    # compute the center of the contour region and draw the
                    # crosshairs
                    M = cv2.moments(approx)
                    (cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
                    (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
                    cv2.line(frame, (startX, cY), (endX, cY), (0, 0, 255), 3)
                    cv2.line(frame, (cX, startY), (cX, endY), (0, 0, 255), 3)

        # draw the status text on the frame
        cv2.putText(frame, status + ", " + qr_status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 255), 2)

        # show the frame and record if a key is pressed
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    cam.release()
    cv2.destroyAllWindows()


class object_detection(object):
    def __init__(self):
        print("Object detection: Class loaded")
