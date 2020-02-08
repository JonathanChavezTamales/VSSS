import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while True:
    gray = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY), 5)

    # Core processing
    
    
    circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10)
    
    if circles is not None:
        cv2.circle(gray, (circles[0][0][0], circles[0][0][1]), circles[0][0][2],  (0,255,0), 5)

    

    cv2.imshow('video', gray)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
