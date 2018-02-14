import libardrone
from time import sleep

drone = libardrone.ARDrone()

drone.takeoff()
sleep(3)
drone.hover()
sleep(5)
drone.land()
sleep(3)
drone.halt()