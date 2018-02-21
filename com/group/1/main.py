import libardrone
import cv2


from time import sleep
drone = libardrone.ARDrone()
cap = cv2.VideoCapture()
cap.open('tcp://192.168.1.1:5555')
drone.takeoff()
sleep(3)
drone.hover()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()



    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sleep(3)
drone.land()
sleep(3)
drone.halt()

cap.release()
cv2.destroyAllWindows()