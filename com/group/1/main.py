# coding=utf-8

# Forbindelse til dronen

# Modtage video optagelse

# Behandle QR kode

# Detektere cirkler eller andre former for geometri

# Reagearer på daqqqqqqqqqqqqta

import cv2

import object_detection

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')


# main method declaration
def main():
    object_detection.detect(cam)


# main method entry point
if __name__ == '__main__':
    main()
