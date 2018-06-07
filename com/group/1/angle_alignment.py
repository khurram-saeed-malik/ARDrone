# coding=utf-8
from math import degrees, atan2
from time import sleep


def angleAlign(drone, rightCorner, leftCorner):
    rightUpperCorner = rightCorner
    rightUpperCorner = str(rightUpperCorner)
    rightUpperCornerX = int(rightUpperCorner.__getslice__(2, 5))
    rightUpperCornerY = int(rightUpperCorner.__getslice__(6, 9))
   # cv2.circle(frame, (rightUpperCornerX, rightUpperCornerY), 30, (0, 60, 180), 4)

    leftUpperCorner = leftCorner
    leftUpperCorner = str(leftUpperCorner)
    leftUpperCornerX = int(leftUpperCorner.__getslice__(2, 5))
    leftUpperCornerY = int(leftUpperCorner.__getslice__(6, 9))
  #  cv2.circle(frame, (leftUpperCornerX, leftUpperCornerY), 30, (0, 60, 180), 4)

    xDiff = rightUpperCornerX - leftUpperCornerX
    yDiff = rightUpperCornerY - leftUpperCornerY
    print(degrees(atan2(xDiff, yDiff)))

    class angle_alignment(object):
        def __init__(self):
            print("Object detection: Class loaded")
