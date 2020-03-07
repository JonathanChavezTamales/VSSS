import math
import cv2
import matplotlib.pyplot as plt
from ColorMatching import *
import numpy as np
import socket
import threading
from object_pb2 import ObjectData

def to255(num, val):
    x = (num*255)//val
    return x

#--------------------------------------------------------------------------------------------------------------

def display(img, cmap = None):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)

#-----------------------------------------------------------------------------------------------------------------

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
    result = cv2.bitwise_and(img, img, mask = mask)
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

def find_robot_center(img, color_code, color1, color2):
    centers1 = find_center(img, color_code, color1)
    centers2 = find_center(img, color_code, color2)

    if not(centers1 is None) and not(centers2 is None):
        c1 = centers1[0]
        c2 = centers2[min_distance(centers1, centers2)]
        robot_center = (c1[0]+c2[0]) // 2, (c1[1]+c2[1]) // 2       
        return c1, c2, robot_center
    return None

#-------------------------------------------------------------------------------------------------------------------

def find_robots(img, color_code, team_color, robot1_color, robot2_color, robot3_color, draw=False):
    try:
        c1_1, c1_2, robot1_center = find_robot_center(img, color_code, robot1_color, team_color)
        c2_1, c2_2, robot2_center = find_robot_center(img, color_code, robot2_color, team_color)
        c3_1, c3_2, robot3_center = find_robot_center(img, color_code, robot3_color, team_color)
    except TypeError:
        return None

    robot1_angle = int(calc_angle(c1_2[0], c1_2[1], c1_1[0], c1_1[1]))
    robot2_angle = int(calc_angle(c2_2[0], c2_2[1], c2_1[0], c2_1[1]))
    robot3_angle = int(calc_angle(c3_2[0], c3_2[1], c3_1[0], c3_1[1]))

    robot1_data = (robot1_center[0], robot1_center[1], robot1_angle)
    robot2_data = (robot2_center[0], robot2_center[1], robot2_angle)
    robot3_data = (robot3_center[0], robot3_center[1], robot3_angle)

    if draw == True:
        cv2.circle(img, robot1_center, 2, (255,255,255), -1)
        cv2.circle(img, robot2_center, 2, (255,255,255), -1)
        cv2.circle(img, robot3_center, 2, (255,255,255), -1)
        cv2.putText(img, text=str(robot1_data), org=(50,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255,255,255), thickness=1)
        cv2.putText(img, text=str(robot2_data), org=(50,100), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255,255,255), thickness=1)
        cv2.putText(img, text=str(robot3_data), org=(50,150), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255,255,255), thickness=1)
    
    return [robot1_data, robot2_data, robot3_data]

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

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

socket = socket.socket()
socket.connect(('10.43.63.47', 4000))
boundaries = color_matching(cap)

hilo = Thread(target=range_selector, args=('l',))
hilo.start()

lastPts = None

while lastPts is None:
    print('looking for colors')
    ret, frame =  cap.read()
    lastPts = find_robots(frame, color_code= "l", team_color="blue", robot1_color="red", robot2_color="purple", robot3_color="pink")
    

while True:

    ret, frame =  cap.read()
   
    if ret:
        
        Pts = find_robots(frame, color_code= "l", team_color="blue", robot1_color="red", robot2_color="purple", robot3_color="pink", draw=True)
        
        if not(Pts is None):
            lastPts = Pts
            robot = ObjectData()
            robot.kind = 1
            robot.id = 0
            robot.team = 1
            robot.x = int(Pts[0][0])
            robot.y = int(Pts[0][1])
            robot.yaw = int(Pts[0][2])
            socket.sendall(robot.SerializeToString())
    
        k = cv2.waitKey(1)
        if k == 27:
            break
        
        cv2.imshow("Frame", frame)
        
cap.release
cv2.destroyAllWindows()