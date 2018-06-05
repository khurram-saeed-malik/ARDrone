# coding=utf-8
from time import sleep


def allign(drone, x, y, w, h):
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

    if 300 < x < 340:
        print("QR is alligned")
        drone.hover()
        #  sleep(2)
        drone.land()


class center_drone(object):
    def __init__(self):
        print("Object detection: Class loaded")
