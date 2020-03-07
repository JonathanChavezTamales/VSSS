import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/jprr2/Videos/Logitech/LogiCapture/cancha_real4.jpg')
img = cv2.medianBlur(img, 7)
external_contours = np.zeros_like(img)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
lab_boundaries = [[200, 120, 120], [255, 170, 170]]

def check_boundaries(boundaries):
    for i, color in enumerate(boundaries):
        for k, val in enumerate(color):
            if boundaries[i][k] < 0:
                boundaries[i][k]=0
            elif boundaries[i][k] > 255:
                    boundaries[i][k]=255

def position(event, x, y, flags, params):

        if event == cv2.EVENT_LBUTTONDOWN:
            lab_boundaries[0][0] = lab_img[y,x,0] - 100
            lab_boundaries[1][0] = lab_img[y,x,0] + 100
            lab_boundaries[0][1] = lab_img[y,x,1] - 6
            lab_boundaries[1][1] = lab_img[y,x,1] + 6
            lab_boundaries[0][2] = lab_img[y,x,2] - 6
            lab_boundaries[1][2] = lab_img[y,x,2] + 6

cv2.namedWindow(winname = "img")
cv2.setMouseCallback("img", position)

while True:

    img = cv2.imread('C:/Users/jprr2/Videos/Logitech/LogiCapture/cancha_real4.jpg')
    img = cv2.medianBlur(img, 7)
    external_contours = np.zeros_like(img)

    check_boundaries(lab_boundaries)

    lower = np.array(lab_boundaries[0], dtype = "uint8")
    upper = np.array(lab_boundaries[1], dtype = "uint8")

    mask = cv2.inRange(lab_img, lower, upper)
    mask = cv2.medianBlur(mask, 7)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) 

    max_lenght = cv2.arcLength(contours[0], True)
    max_contour = 0

    for i, contour in enumerate(contours):
        
        if hierarchy[0][i][3] == -1:          #Cheking the last element of each list in hierarchy - If it equals -1, thats means it is an external contour
            lenght = cv2.arcLength(contours[i], True)
            
            if lenght > max_lenght:
                max_lenght = lenght
                max_contour = i

    cv2.drawContours(image = external_contours, contours = contours, contourIdx = max_contour, color = (255,255,255), thickness = 2)
    
    esquinas = [[10000,10000], [0,10000], [10000,0], [0,0]]
    conv_hull = cv2.convexHull(contours[max_contour])

    for j in range(4):
        for i in conv_hull:
            x, y = i.ravel()
            if j == 0:
                if (x +y) <= (esquinas[j][0] + esquinas[j][1]):
                    esquinas[j][0] = x
                    esquinas[j][1] = y
            elif j == 1:
                if y <= esquinas[j][1] and (x >= esquinas[j][0] or abs(x - esquinas[j][0]) <= 50):
                        esquinas[j][0] = x
                        esquinas[j][1] = y
            elif j == 2:
                if x <= esquinas[j][0] and (y >= esquinas[j][1] or abs(y - esquinas[j][1]) <= 50):
                        esquinas[j][0] = x
                        esquinas[j][1] = y
            elif j == 3:
                if (x +y) >= (esquinas[j][0] + esquinas[j][1]):
                    esquinas[j][0] = x
                    esquinas[j][1] = y

    cX = (esquinas[0][0] + esquinas[3][0]) // 2
    cY = (esquinas[1][1] + esquinas[2][1]) // 2
        
    for [x, y] in esquinas:
        cv2.circle(img, (x,y), 5, (0,0,255), -1)

    cv2.line(img, tuple(esquinas[0]), tuple(esquinas[3]), (255,0,0), 2)
    cv2.line(img, tuple(esquinas[1]), tuple(esquinas[2]), (255,0,0), 2)
    cv2.circle(img, (cX, cY), 10, (0,255,0), -1)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('contours', external_contours)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
print(conv_hull)
print(esquinas)