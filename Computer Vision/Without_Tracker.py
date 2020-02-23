import math
import cv2
import matplotlib.pyplot as plt
from ColorMatching import *
import numpy as np

def to255(num, val):
    x = (num*255)//val
    return x

#--------------------------------------------------------------------------------------------------------------

def display(img, cmap = None):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)

#-----------------------------------------------------------------------------------------------------------------

def find_center(img, color, color_code):
    centers = []
    kernel = np.ones(shape = (4,4), dtype = np.uint8)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    if color == "orange":
        lower = np.array(boundaries[2][0], dtype = "uint8")
        upper = np.array(boundaries[2][1], dtype = "uint8")
    elif color == "red":
        lower = np.array(boundaries[3][0], dtype = "uint8")
        upper = np.array(boundaries[3][1], dtype = "uint8")
    elif color == "green":
        lower = np.array(boundaries[4][0], dtype = "uint8")
        upper = np.array(boundaries[4][1], dtype = "uint8")
    elif color == "pink":
        lower = np.array(boundaries[6][0], dtype = "uint8")
        upper = np.array(boundaries[6][1], dtype = "uint8")
    elif color == "purple":
        lower = np.array(boundaries[5][0], dtype = "uint8")
        upper = np.array(boundaries[5][1], dtype = "uint8")
    elif color == "yellow":
        lower = np.array(boundaries[0][0], dtype = "uint8")
        upper = np.array(boundaries[0][1], dtype = "uint8")
    elif color == "blue":
        lower = np.array(boundaries[1][0], dtype = "uint8")
        upper = np.array(boundaries[1][1], dtype = "uint8")
     
    mask = cv2.inRange(hsv_img, lower, upper)
    result = cv2.bitwise_and(rgb_img, rgb_img, mask = mask)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    eroded = cv2.erode(thresh, kernel, iterations = 1)
    dilated = cv2.dilate(eroded, kernel, iterations = 2)

    image, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

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

#-------------------------------------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------------------------------------

def draw_line(img, c1, c2):
    min_c = min_distance(c1, c2)
    cv2.line(img, c1[0], c2[min_c], color = 255, thickness = 2)
    cv2.circle(img, c1[0], radius = 3, color = (0,255,0), thickness = -1)
    cv2.circle(img, c2[min_c], radius = 3, color = (0,255,0), thickness = -1)
    return img

#-------------------------------------------------------------------------------------------------------------------

def find_robot_center(img, color1, color2):
    centers1 = find_center(img, color1)
    centers2 = find_center(img, color2)
    
    if centers1 != None and centers2 != None:
        c1 = centers1[0]
        c2 = centers2[min_distance(centers1, centers2)]
        robot_center = (c1[0]+c2[0]) // 2, (c1[1]+c2[1]) // 2
        return np.asarray(c1, c2, robot_center, dtype = np.float32)
    return None

#--------------------------------------------------------------------------------------------------------------------

def calc_angle(x1, y1, x2, y2):
    if x2>x1 and y1==y2:
        return 0
    elif x1>x2 and y1==y2:
        return 180
    elif x1==x2 and y1>y2:
        return 90
    elif x1==x2 and y2>y1:
        return 270
    
    ang = math.atan((y2-y1)/(x2-x1)) * (180/math.pi)
    
    if x2>x1 and y1>y2:
        return abs(ang)
    elif x2>x1 and y2>y1:
        return 360 - abs(ang)
    elif x1>x2 and y1>y2:
        return 180 - abs(ang)
    elif x1>x2 and y2>y1:
        return 180 + abs(ang)
    
#----------------------------------------------------------------------------------------------------------------------

Radius=0.03        #metros
Moment=0.06        #distancia entre llantas - metros
k=1                #ganancia
v=0.6              # m/s
w_max=31.42        # rad/s 

def F_Control (x_robot, y_robot, theta, x_ball, y_ball):
    diff_x = x_ball - x_robot
    diff_y = y_ball - y_robot

    required_theta = np.arctan2(diff_y, diff_x)*180/np.pi
    diff_theta = required_theta - theta

    w = k*diff_theta

    w_right = (v/Radius) + (0.5*w/Moment/Radius)
    w_left = (v/Radius) - (0.5*w/Moment/Radius)

    if (w_right>w_max):
        w_right = w_max

    if (w_left>w_max):
        w_left = w_max

    pwm_right = w_right/w_max*255
    pwm_left = w_left/w_max*255

    return pwm_right, pwm_left

#--------------------------------------------------------------------------------------------------------------------------------

boundaries = color_matching()
hsv_boundaries = boundaries[0]
rgb_boundaries = boundaries[1]
lab_boundaries = boundaries[2]

cap = cv2.VideoCapture(0)

lastPts = None

while lastPts is None:
    print('looking for colors')
    lastPts = find_robot_center(frame, "red", "blue")
    

while True:

    ret, frame =  cap.read()
    
    #frame = frame[:, 190:1050, :]

    #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if ret:
        
        Pts = find_robot_center(frame, "red", "blue")
        
        if not(Pts is None):
            lastPts = Pts
        
        #x2 = lastPts[0][0][0]
        #y2 = lastPts[0][0][1]
        #c2 = (x2, y2)
        #x1 = lastPts[1][0][0]
        #y1 = lastPts[1][0][1]
        #c1 = (x1, y1)
        cX = lastPts[2][0][0]
        cY = lastPts[2][0][1]
        center = (cX, cY)
        
        ang = calc_angle(x1, y1, x2, y2)
        
        cv2.circle(frame, center, radius = 5, color = (0,255,0), thickness = -1)
        cv2.putText(frame, text = str(ang), org = (100,100), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,255,0), thickness = 1)
        cv2.putText(frame, text = str(center), org = (100,300), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,255,0), thickness = 1)
        #cv2.putText(frame, text = str(c1), org = (100,350), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (255,0,0), thickness = 1)
        #cv2.putText(frame, text = str(c2), org = (100,400), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,255,255), thickness = 1)
        
        k = cv2.waitKey(1)

        if k == 27:
            break
        
        cv2.imshow("Frame", frame)
        
cap.release
cv2.destroyAllWindows()