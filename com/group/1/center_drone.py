# coding=utf-8
from time import sleep


def allign(drone, x, y, w):
    if x < 240 and w < 80:
        print("QR is right to the center and far, moving left")
        drone.move_left()
        sleep(0.5)
        drone.hover()
        sleep(0.7)
        # sleep(2)

    if x < 280 and 80 < w < 100:
        print("QR is right to the center and medium distance, moving left")
        drone.move_left()
        sleep(0.35)
        drone.hover()
        sleep(0.7)
        # sleep(2)

    if x < 280 and 100 < w:
        print("QR is right to the center and close, moving left")
        drone.move_left()
        sleep(0.3)
        drone.hover()
        sleep(0.7)

    if x > 370 and w < 80:
        print("QR is left to the center and far, moving right")
        drone.move_right()
        sleep(0.5)
        drone.hover()
        sleep(0.7)
    # sleep(2)

    if x > 340 and 80 < w < 100:
        print("QR is left to the center and medium distance, moving right")
        drone.move_right()
        sleep(0.35)
        drone.hover()
        sleep(0.7)

    if x > 340 and 100 < w:
        print("QR is left to the center and close, moving right")
        drone.move_right()
        sleep(0.3)
        drone.hover()
        sleep(0.7)

    if y < 140:
        print("QR is under the center, moving up")
        drone.hover()
        sleep(0.4)
        drone.move_up()
        sleep(0.3)
        drone.hover()
        sleep(0.5)
    #  sleep(2)

    if y > 220:
        print("QR is over the center, moving down")
        drone.hover()
        sleep(0.5)
        drone.move_down()
        sleep(0.3)
        drone.hover()
        sleep(0.5)
    #  sleep(2)


class center_drone(object):
    def __init__(self):
        print("Object detection: Class loaded")
