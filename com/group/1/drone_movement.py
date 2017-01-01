from time import sleep


def drone_adjust(cX, cY, w, drone):
    # if 300 < cX < 340 and 140 < cY < 220:
    print("QR is alligned")
    if w < 80:
        drone.move_forward()
        sleep(0.5)
        drone.hover()
        sleep(1)
    if 80 < w < 110:
        drone.move_forward()
        sleep(0.4)
        drone.hover()
        sleep(1)
    if 110 < w < 130:
        drone.move_forward()
        sleep(0.3)
        drone.hover()
        sleep(1)


def move_through_circle(drone):
    print("Drone is close to QR, moving through")
    drone.move_up()
    sleep(1.35)
    drone.hover()
    sleep(0.5)
    drone.move_forward()
    sleep(1.5)
    drone.hover()
    sleep(1)
    drone.move_down()
    sleep(1)
    drone.hover()
    sleep(1)


def turn_right(drone):
    drone.hover()
    sleep(1)
    drone.turn_right()
    sleep(0.5)
    drone.turn_left()
    sleep(0.1)
    drone.hover()
    sleep(1)
