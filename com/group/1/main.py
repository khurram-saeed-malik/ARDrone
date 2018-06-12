# coding=utf-8
import cv2
from lib import libardrone
import object_detection

drone = libardrone.ARDrone()
cam = cv2.VideoCapture('tcp://192.168.1.1:5555')


# main method declaration
def main():
    object_detection.detect(cam)


# main method entry point
if __name__ == '__main__':
    main()