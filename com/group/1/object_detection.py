# coding=utf-8

import cv2
import re
import qr_reader
from time import sleep


def detect(cam, drone, count):
    qr_value = 4
    frame = cam.read()
    # error reading frame
    if not cam.read():
        print 'Problem reading cam feed'

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)

    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # ensure that the approximated contour is "roughly" rectangular
        if 4 <= len(approx) <= 6:
            # compute the bounding box of the approximated contour and
            # use the bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)

            # compute the solidity of the original contour
            area = cv2.contourArea(c)
            hull_area = cv2.contourArea(cv2.convexHull(c))
            solidity = area / float(hull_area)

            # compute whether or not the width and height, solidity, and
            # aspect ratio of the contour falls within appropriate bounds
            keep_dims = w > 15 and h > 15
            keep_solidity = solidity > 0.9
            keep_aspect_ratio = 0.8 >= aspect_ratio >= 0.5

            # ensure that the contour passes all our tests
            if keep_dims and keep_solidity and keep_aspect_ratio:
                print "Found square(s)"

                # detect qr
                qr = qr_reader.read(gray)
                match = re.search(r'P\.\d{2}', str(qr))
                if match:
                    # todo: logic for different qr codes
                    # drone.land()
                    if qr == 'P.0' + repr(qr_value):
                        print('Correct QR, value is P.0' + repr(qr_value))

                        # drone.speed = 0.5
                        # drone.move_up()
                        # sleep(1.5)
                        # drone.speed = 0.2
                        # drone.move_forward()
                        # sleep(3)
                        # drone.hover()
                        # sleep(1)
                        # drone.hover(1)
                        # drone.land()
                        # sleep(5)
                        # drone.reset()
                        drone.land()
                        sleep(3)
                        drone.halt()
                        cam.release()
                        cv2.destroyAllWindows()
                        # qr_value += 1
                        return
                    else:
                        print 'Not correct QR'

                else:
                    print 'No QR in rectangle'
                    drone.turn_right()
                    sleep(0.3)
                    drone.hover()
                    sleep(3)

                # compute the center of the contour region and draw the crossbars
                M = cv2.moments(approx)
                (cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
                (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
                cv2.line(frame, (startX, cY), (endX, cY), (0, 0, 255), 3)
                cv2.line(frame, (cX, startY), (cX, endY), (0, 0, 255), 3)
                # center_drone.allign(drone, centerX, centerY, w, h)
                print 'Crosshair > ' + str(cX) + ',' + str(cY)
                # todo move right or left | turn right or left | go down or up
                return detect(cam, drone, 5)

            else:
                if count != 0:
                    print('No rectangle found turning around')
                    drone.turn_right()
                    sleep(0.15)
                    drone.turn_left()
                    sleep(0.01)
                    drone.hover()
                    sleep(3)
                    return detect(cam, drone, count - 1)
                else:
                    drone.land()
                    drone.halt()
                    cam.release()
                    return


class object_detection(object):
    def __init__(self):
        print("Object detection: Class loaded")
