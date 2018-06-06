import cv2
import numpy


# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
# cam = cv2.VideoCapture('tcp://192.168.1.1:5555')

def main():
    image = cv2.imread("circle.png", 0)
    image = cv2.medianBlur(image, 5)
    cimage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = numpy.uint16(numpy.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimage, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimage, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimage)
    cv2.resizeWindow('image', 600, 600)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # TODO: Detect circles with only red boundaries


if __name__ == '__main__':
    main()
