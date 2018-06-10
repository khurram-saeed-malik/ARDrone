# coding=utf-8
from time import sleep
import thread
import cv2
from lib import libardrone
import capture
import object_detection

drone = libardrone.ARDrone()
# 'tcp://192.168.1.1:5555'
cam = cv2.VideoCapture(0)


# main method declaration
def main():
    try:
        thread.start_new_thread(flying(), ())
        thread.start_new_thread(video(), ())
    except:
        print 'Error> Unable to start threads..'


def flying():
    #drone.takeoff()
    #sleep(4)
    object_detection.detect(cam, drone, 10)


def video():
    capture.video_feed(cam, drone)


# main method entry point
if __name__ == '__main__':
    main()
