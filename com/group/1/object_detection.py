# coding=utf-8
from time import sleep
from lib import libardrone
import cv2
import re
import qr_reader
import center_drone

drone = libardrone.ARDrone()


def detect(cam):
    index = 1
    qr_value = 2
    drone.takeoff()
    sleep(3)
    running = True

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
                cam.release()
                cv2.destroyAllWindows()
                break
        else:
            # error reading frame
            print 'error reading video feed'

        if index % 45 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imwrite("pic1_grascayle.png", gray)
            # Hvad bruger vi dem til?:
            blurred = cv2.GaussianBlur(gray, (7, 7), 0)
            # cv2.imwrite("pic2_blurred.png", blurred)
            edged = cv2.Canny(blurred, 50, 150)
            # cv2.imwrite("pic3_edged.png", edged)
            # print 'DONE TAKING IMAGES'

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
                    keep_aspect_ratio = aspect_ratio <= 0.8 and aspect_ratio >= 0.5

                    # ensure that the contour passes all our tests
                    if keep_dims and keep_solidity and keep_aspect_ratio:
                        # draw an outline around the target and update the status
                        # text
                        cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
                        status = "Found square(s)"

                        print(x, y, w, h)

                        # todo move right or left | turn right or left | go down or up

                        # compute the center of the contour region and draw the crossbars
                        M = cv2.moments(approx)
                        (cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                        (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
                        (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
                        cv2.line(frame, (startX, cY), (endX, cY), (0, 0, 255), 3)
                        cv2.line(frame, (cX, startY), (cX, endY), (0, 0, 255), 3)
                        center_drone.allign(drone, cX, cY, w, h)

                        # detect qr
                        qr = qr_reader.read(gray)
                        match = re.search(r'P\.\d{2}', str(qr))
                        if match:
                            # todo: logic for different qr codes
                            # drone.land()
                            if qr == 'P.0' + repr(qr_value):
                                print('Correct QR, value is P.0' + repr(qr_value))

                                if 290 < cX < 350 and 140 < cY < 220:
                                    print("QR is alligned")
                                    drone.move_forward()
                                    sleep(0.7)
                                    drone.hover()
                                if w > 105:
                                    print("Drone is close to QR, moving through")
                                    sleep(2)
                                    drone.hover()
                                    sleep(2)
                                    drone.move_up()
                                    sleep(1)
                                    drone.hover()
                                    sleep(1)
                                    drone.move_forward()
                                    sleep(1.3)
                                    drone.hover()
                                    sleep(1)
                                    drone.move_down()
                                    sleep(1)
                                    drone.hover()
                                    sleep(1)
                                    qr_value += 1
                                    break

                            else:
                                print 'Not correct QR'

                        else:
                            print 'rectangle is not a QR'

        index += 1

        # draw the status text on the frame
        cv2.putText(frame, status + ", " + qr_status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 255), 2)

        # show the frame
        cv2.imshow("Frame", frame)

    cam.release()
    cv2.destroyAllWindows()


class object_detection(object):
    def __init__(self):
        print("Object detection: Class loaded")
