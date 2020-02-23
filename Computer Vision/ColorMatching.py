import cv2
import numpy as np
from ExitWindow import *
from RangeSelector import *
#import matplotlib.pyplot

def to255(num, val):
    x = (num*255)//val
    return x
pip
def check_boundaries(boundaries):
    for i, color in enumerate(boundaries):
        for j, channels in enumerate(color):
            for k, val in enumerate(channels):
                if boundaries[i][j][k] < 0:
                    boundaries[i][j][k]=0
                elif boundaries[i][j][k] > 255:
                     boundaries[i][j][k]=255
                        
def color_matching():
    cap = cv2.VideoCapture(0)

    hsv_boundaries = [[[0,0,0],[255,255,255]],  #AMARILLO
                     [[0,0,0],[255,255,255]],   #AZUL
                     [[0,0,0],[255,255,255]],   #NARANJA
                     [[0,0,0],[255,255,255]],   #ROJO
                     [[0,0,0],[255,255,255]],   #VERDE
                     [[0,0,0],[255,255,255]],   #MORADO
                     [[0,0,0],[255,255,255]]]   #ROSA

    rgb_boundaries = [[[0,0,0],[255,255,255]],  #AMARILLO
                     [[0,0,0],[255,255,255]],   #AZUL
                     [[0,0,0],[255,255,255]],   #NARANJA
                     [[0,0,0],[255,255,255]],   #ROJO
                     [[0,0,0],[255,255,255]],   #VERDE
                     [[0,0,0],[255,255,255]],   #MORADO
                     [[0,0,0],[255,255,255]]]   #ROSA

    lab_boundaries = [[[0,0,0],[255,255,255]],  #AMARILLO
                     [[0,0,0],[255,255,255]],   #AZUL
                     [[0,0,0],[255,255,255]],   #NARANJA
                     [[0,0,0],[255,255,255]],   #ROJO
                     [[0,0,0],[255,255,255]],   #VERDE
                     [[0,0,0],[255,255,255]],   #MORADO
                     [[0,0,0],[255,255,255]]]   #ROSA


    def position(event, x, y, flags, params):
        global cX, cY
        cX, cY = x, y

        if event == cv2.EVENT_LBUTTONDOWN:
            if code == 'h':
                hsv_boundaries[color][0][0] = hsv_img[y,x,0] - 10
                hsv_boundaries[color][1][0] = hsv_img[y,x,0] + 10
                hsv_boundaries[color][0][1] = hsv_img[y,x,1] - 45
                hsv_boundaries[color][1][1] = hsv_img[y,x,1] + 45
                hsv_boundaries[color][0][2] = hsv_img[y,x,2] - 45
                hsv_boundaries[color][1][2] = hsv_img[y,x,2] + 45

            elif code == 'r':
                rgb_boundaries[color][0][0] = rgb_img[y,x,0] - 30
                rgb_boundaries[color][1][0] = rgb_img[y,x,0] + 30
                rgb_boundaries[color][0][1] = rgb_img[y,x,1] - 30
                rgb_boundaries[color][1][1] = rgb_img[y,x,1] + 30
                rgb_boundaries[color][0][2] = rgb_img[y,x,2] - 30
                rgb_boundaries[color][1][2] = rgb_img[y,x,2] + 30

            elif code == 'l':
                lab_boundaries[color][0][0] = lab_img[y,x,0] - 80
                lab_boundaries[color][1][0] = lab_img[y,x,0] + 80
                lab_boundaries[color][0][1] = lab_img[y,x,1] - 10
                lab_boundaries[color][1][1] = lab_img[y,x,1] + 10
                lab_boundaries[color][0][2] = lab_img[y,x,2] - 10
                lab_boundaries[color][1][2] = lab_img[y,x,2] + 10


    cX = 0
    cY = 0
    code = 'h'
    color = 0
    cv2.namedWindow(winname = "Colors")
    cv2.setMouseCallback("Colors", position)

    while True:

        ret, frame = cap.read()
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lab_img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        check_boundaries(hsv_boundaries)
        check_boundaries(rgb_boundaries)
        check_boundaries(lab_boundaries)

        k = cv2.waitKey(1)
        if k == 27:
            quit = exit_window()
            if quit: break
        elif k == ord("h"):
            code = 'h'        
        elif k == ord("r"):
            code = 'r'
        elif k == ord("l"):
            code = 'l'
        elif k >= 0 and chr(k).isdigit():
            if int(chr(k)) <= 6:
                color = int(chr(k))

        if color == 0:
            cv2.putText(frame, "Color: Amarillo", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[0][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[0][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[0][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[0][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[0][0], dtype = "uint8")
                upper = np.array(lab_boundaries[0][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 1:
            cv2.putText(frame, "Color: Azul", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[1][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[1][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[1][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[1][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[1][0], dtype = "uint8")
                upper = np.array(lab_boundaries[1][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 2:
            cv2.putText(frame, "Color: Naranja", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[2][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[2][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[2][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[2][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[2][0], dtype = "uint8")
                upper = np.array(lab_boundaries[2][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 3:
            cv2.putText(frame, "Color: Rojo", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[3][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[3][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[3][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[3][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[3][0], dtype = "uint8")
                upper = np.array(lab_boundaries[3][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 4:
            cv2.putText(frame, "Color: Verde", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[4][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[4][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[4][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[4][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[4][0], dtype = "uint8")
                upper = np.array(lab_boundaries[4][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 5:
            cv2.putText(frame, "Color: Morado", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[5][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[5][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[5][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[5][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[5][0], dtype = "uint8")
                upper = np.array(lab_boundaries[5][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

        elif color == 6:
            cv2.putText(frame, "Color: Rosa", org = (50, 200), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (255,255,255), thickness = 1)

            if code == 'h':
                cv2.putText(frame, f"H: {hsv_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"S: {hsv_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                cv2.putText(frame, f"V: {hsv_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = 255, thickness = 1)
                lower = np.array(hsv_boundaries[6][0], dtype = "uint8")
                upper = np.array(hsv_boundaries[6][1], dtype = "uint8")
                mask = cv2.inRange(hsv_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'r':
                cv2.putText(frame, f"R: {rgb_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"G: {rgb_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                cv2.putText(frame, f"B: {rgb_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (0,0,255), thickness = 1)
                lower = np.array(rgb_boundaries[6][0], dtype = "uint8")
                upper = np.array(rgb_boundaries[6][1], dtype = "uint8")
                mask = cv2.inRange(rgb_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)

            elif code == 'l':
                cv2.putText(frame, f"L: {lab_img[cY,cX,0]}", org = (50, 50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"A: {lab_img[cY,cX,1]}", org = (50, 100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                cv2.putText(frame, f"B: {lab_img[cY,cX,2]}", org = (50, 150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (100,230,150), thickness = 1)
                lower = np.array(lab_boundaries[6][0], dtype = "uint8")
                upper = np.array(lab_boundaries[6][1], dtype = "uint8")
                mask = cv2.inRange(lab_img, lower, upper)
                result = cv2.bitwise_and(frame, frame, mask = mask)


        cv2.imshow("Colors", frame)
        cv2.imshow("Mask", result)

    cap.release()
    cv2.destroyAllWindows()
    return hsv_boundaries, rgb_boundaries, lab_boundaries

boundaries = color_matching()