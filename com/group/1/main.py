# coding=utf-8
# TODOS:
# Forbinde til dronen

# Modtage video optagelse

# Behandle QR kode

# Detektere cirkler eller andre former for geometri

# Reagearer på data

import sys
import cv2
import object_detection

sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
# sys.path.insert(0, 'C:\Python\Lib\site-packages')
# sys.path.insert(0, '/home/bf/.local/lib/python2.7/site-packages')

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')


def main():

    object_detection.detect(cam)


if __name__ == '__main__':
    main()
