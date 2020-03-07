from Robot import Robot
from ColorMatching import *
import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

boundaries = color_matching(cap)

robot1 = Robot('red', 'blue', boundaries)
robot2 = Robot('purple', 'blue', boundaries)
robot3 = Robot('orange', 'yellow', boundaries)
robot4 = Robot('pink', 'yellow', boundaries)
robot5 = Robot('green', 'yellow', boundaries)

while True:


    ret, frame = cap.read()

    robot1.find(frame, 'l')
    robot1.show(frame)
    robot2.find(frame, 'l')
    robot2.show(frame)
    robot3.find(frame, 'l')
    robot3.show(frame)
    robot4.find(frame, 'l')
    robot4.show(frame)
    robot5.find(frame, 'l')
    robot5.show(frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()