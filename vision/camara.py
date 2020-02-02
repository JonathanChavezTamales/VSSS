import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)

    cv2.putText(frame, "Slow Method", (10, 30),	cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
    # Display the resulting frame
    cv2.imshow('window name',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
