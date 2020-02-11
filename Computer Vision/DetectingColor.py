import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def display(img, cmap = None):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)
    
def to255(num, val):
    x = (num*255)//val
    return x

cap = cv2.VideoCapture(0)

boundaries = [
        ([0, to255(30,100), to255(50,100)], [to255(30,360), to255(100,100), to255(100,100)]),
    
        ([to255(0,360), to255(35,100), to255(20,100)], [to255(30,360), to255(100,100), to255(100,100)]),  #ORANGE
    
        ([to255(80,360), to255(10,100), to255(65,100)], [to255(140,360), to255(100,100), to255(100,100)]),
        ([to255(40,360), to255(0,100), to255(75,100)], [to255(65,360), to255(60,100), to255(100,100)])]

lower = np.array(boundaries[1][0], dtype = "uint8")
upper = np.array(boundaries[1][1], dtype = "uint8")

while True:

    ret, img = cap.read()
    #img = cv2.imread("C:/Users/jprr2/Videos/Logitech/LogiCapture/4_colors.jpg")
    #rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if ret: 
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv_img, lower, upper)
        result = cv2.bitwise_and(img, img, mask = mask)

        k = cv2.waitKey(1)
        if k == 27:
            break

        cv2.imshow("ORANGE", result)
        
cap.release()
cv2.destroyAllWindows()

#display(rgb_img)