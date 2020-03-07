import cv2
import numpy as np
from ExitWindow import *
from ColorMatching import *
import matplotlib.pyplot as plt
import math

def find_center(img, color_code, color):
    global boundaries
    centers = []
    kernel = np.ones(shape = (3,3), dtype = np.uint8)
    if color_code == 'h':
        selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        selected_boundaries = boundaries[0]

    elif color_code == 'r':
        selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        selected_boundaries = boundaries[1]

    elif color_code == 'l':
        selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        selected_boundaries = boundaries[2]
    
    if color == "orange":
        lower = np.array(selected_boundaries[2][0], dtype = "uint8")
        upper = np.array(selected_boundaries[2][1], dtype = "uint8")
    elif color == "red":
        lower = np.array(selected_boundaries[3][0], dtype = "uint8")
        upper = np.array(selected_boundaries[3][1], dtype = "uint8")
    elif color == "green":
        lower = np.array(selected_boundaries[4][0], dtype = "uint8")
        upper = np.array(selected_boundaries[4][1], dtype = "uint8")
    elif color == "pink":
        lower = np.array(selected_boundaries[6][0], dtype = "uint8")
        upper = np.array(selected_boundaries[6][1], dtype = "uint8")
    elif color == "purple":
        lower = np.array(selected_boundaries[5][0], dtype = "uint8")
        upper = np.array(selected_boundaries[5][1], dtype = "uint8")
    elif color == "yellow":
        lower = np.array(selected_boundaries[0][0], dtype = "uint8")
        upper = np.array(selected_boundaries[0][1], dtype = "uint8")
    elif color == "blue":
        lower = np.array(selected_boundaries[1][0], dtype = "uint8")
        upper = np.array(selected_boundaries[1][1], dtype = "uint8")
     
    mask = cv2.inRange(selected_img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    eroded = cv2.erode(thresh, kernel, iterations = 1)
    dilated = cv2.dilate(eroded, kernel, iterations = 2)

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for i in contours:
        
            conv_hull = cv2.convexHull(i)

            top    = tuple(conv_hull[conv_hull[:,:,1].argmin()][0])
            bottom = tuple(conv_hull[conv_hull[:,:,1].argmax()][0])
            left   = tuple(conv_hull[conv_hull[:,:,0].argmin()][0])
            right  = tuple(conv_hull[conv_hull[:,:,0].argmax()][0])

            cX = (left[0] + right[0]) // 2
            cY = (top[1] + bottom[1]) // 2

            centers.append((cX, cY))     
        return centers
    return None

def find_robot_center(img, color_code, color1, color2):

    print('aqui ando')
    centers1 = find_center(img, color_code, color1)
    centers2 = find_center(img, color_code, color2)

    if not(centers1 is None) and not(centers2 is None):
        c1 = centers1[0]
        c2 = centers2[min_distance(centers1, centers2)]
        robot_center = (c1[0]+c2[0]) // 2, (c1[1]+c2[1]) // 2            
        return c1, c2, robot_center
    return None

def min_distance(pt1, iterable):
    x1 = pt1[0][0]
    y1 = pt1[0][1]
    min_distance = 10000000
    min_center = 0
    for i, (x2, y2) in enumerate(iterable):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if distance < min_distance:
            min_distance = distance
            min_center = i 
    return min_center


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

boundaries = color_matching(cap)

while True:

    ret, frame = cap.read()

    if ret:

        try:
            c1, c2, robot_center = find_robot_center(frame, 'l', 'orange', 'blue')    
            cv2.circle(frame, robot_center, 10, (255,255,255), -1)
        except TypeError:
            pass


        cv2.imshow("frame", frame)

        k = cv2.waitKey(1)
        
        if k == 27:
            break

        

cap.release
cv2.destroyAllWindows()





#cap.release()
#cv2.destroyAllWindows()