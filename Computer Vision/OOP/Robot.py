import cv2
import numpy as np
import math


class Robot():
    def __init__(self, color, team, boundaries):
        self.color = color
        self.team = team
        self.position = None
        self.angle = None
        self.boundaries = boundaries

    def find(self, img, color_code):
        def find_individual_color(img, color_code):
            centers = []
            kernel = np.ones(shape = (3,3), dtype = np.uint8)
            if color_code == 'h':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                selected_boundaries = self.boundaries[0]

            elif color_code == 'r':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                selected_boundaries = self.boundaries[1]

            elif color_code == 'l':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
                selected_boundaries = self.boundaries[2]
            
            if self.color == "orange":
                lower = np.array(selected_boundaries[2][0], dtype = "uint8")
                upper = np.array(selected_boundaries[2][1], dtype = "uint8")
            elif self.color == "red":
                lower = np.array(selected_boundaries[3][0], dtype = "uint8")
                upper = np.array(selected_boundaries[3][1], dtype = "uint8")
            elif self.color == "green":
                lower = np.array(selected_boundaries[4][0], dtype = "uint8")
                upper = np.array(selected_boundaries[4][1], dtype = "uint8")
            elif self.color == "pink":
                lower = np.array(selected_boundaries[6][0], dtype = "uint8")
                upper = np.array(selected_boundaries[6][1], dtype = "uint8")
            elif self.color == "purple":
                lower = np.array(selected_boundaries[5][0], dtype = "uint8")
                upper = np.array(selected_boundaries[5][1], dtype = "uint8")
            
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

        def find_team_color(img, color_code):
            centers = []
            kernel = np.ones(shape = (3,3), dtype = np.uint8)
            if color_code == 'h':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                selected_boundaries = self.boundaries[0]

            elif color_code == 'r':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                selected_boundaries = self.boundaries[1]

            elif color_code == 'l':
                selected_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
                selected_boundaries = self.boundaries[2]
            
            if self.team == "yellow":
                lower = np.array(selected_boundaries[0][0], dtype = "uint8")
                upper = np.array(selected_boundaries[0][1], dtype = "uint8")
            elif self.team == "blue":
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



        centers1 = find_individual_color(img, color_code)
        centers2 = find_team_color(img, color_code)

        if not(centers1 is None) and not(centers2 is None):
            c1 = centers1[0]
            c2 = centers2[min_distance(centers1, centers2)]
            robot_center = (c1[0]+c2[0]) // 2, (c1[1]+c2[1]) // 2       
            self.position = robot_center
            self.angle = calc_angle(c2[0], c2[1], c1[0], c1[1])

    def show(self, img):
        cv2.circle(img, self.position, 2, (255,255,255), -1)