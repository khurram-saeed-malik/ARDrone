# coding=utf-8
from time import sleep
import thread
import cv2
from lib import libardrone
import capture
import object_detection

drone = libardrone.ARDrone()

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')


# main method declaration
def main():
    # try:
    #     thread.start_new_thread(video(), ())
    #     thread.start_new_thread(flying(), ())
    # except:
    #     print 'Error> Unable to start threads..'
    flying()


def flying():
    drone.takeoff()
    sleep(4)
    object_detection.detect(cam, drone, 10)


def video():
    capture.video_feed(cam, drone)


# main method entry point
if __name__ == '__main__':
    main()
