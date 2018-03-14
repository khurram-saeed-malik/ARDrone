# coding=utf-8
# TODOS:
# Forbinde til dronen

# Modtage video optagelse

# Behandle QR kode

# Detektere cirkler eller andre former for geometri

# Reagearer på data

import sys

sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
# sys.path.insert(0, 'C:\Python\Lib\site-packages')
# sys.path.insert(0, '/home/bf/.local/lib/python2.7/site-packages')
import cv2
import QRReader
import object_detection

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
qr_reader = QRReader


def main():
    qr_code_detected = False
    running = True
    x = 1

    while qr_code_detected:
        code = qr_reader.read(greyscale_img)
        if code == 'P.0' + x:
            return True


    object_detection.detect(cam)


if __name__ == '__main__':
    main()
