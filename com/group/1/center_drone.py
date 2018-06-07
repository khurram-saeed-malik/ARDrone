# coding=utf-8
from time import sleep
from lib import libardrone


drone = libardrone.ARDrone()


def allign(x,y,w,h):

    if x < 300:
        print("QR is right to the center, moving left")
        drone.move_left()
        sleep(0.01)
        drone.hover()
      #  sleep(2)

    if x > 340:
        print("QR is left to the center, moving right")
        drone.move_right()
        sleep(0.01)
        drone.hover()
       # sleep(2)

    if 300 < x < 340 and 140 < y < 220:
        print("QR is alligned")
        drone.hover()
      #  sleep(2)
        drone.land()

    if y < 140:
        print("QR is under the center, moving up")
        drone.move_up()
        sleep(0.01)
        drone.hover()
      #  sleep(2)

    if y > 220:
        print("QR is over the center, moving down")
        drone.move_down()
        sleep(0.01)
        drone.hover()
    #  sleep(2)

class center_drone(object):
    def __init__(self):
     print("Object detection: Class loaded")