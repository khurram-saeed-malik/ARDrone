# coding=utf-8
from time import sleep
from lib import libardrone


def allign(drone, x, y, w, h):
    if x < 290:
        print("QR is right to the center, moving left")
        drone.move_left()
        sleep(0.3)
        drone.hover()
        sleep(0.5)
        #sleep(2)

    if x > 350:
        print("QR is left to the center, moving right")
        drone.move_right()
        sleep(0.3)
        drone.hover()
        sleep(0.5)
    # sleep(2)

    if 290 < x < 350 and 140 < y < 220:
        print("QR is alligned")
        drone.move_forward()
        sleep(0.7)
        drone.hover()

    if y < 140:
        print("QR is under the center, moving up")
        drone.hover()
        sleep(0.4)
        drone.move_up()
        sleep(0.4)
        drone.hover()
        sleep(0.5)
    #  sleep(2)

    if y > 220:
        print("QR is over the center, moving down")
        drone.hover()
        sleep(0.5)
        drone.move_down()
        sleep(0.5)
        drone.hover()
        sleep(0.5)
    #  sleep(2)
    if w > 130:
        print("Drone is close to QR, moving through")
        sleep(2)
        drone.hover()
        sleep(2)
        drone.move_up()
        sleep(3)
        drone.hover()
        sleep(1)
        drone.move_forward()
        sleep(2)
        drone.hover()
        sleep(0.5)
        drone.land()


class center_drone(object):
    def __init__(self):
        print("Object detection: Class loaded")
