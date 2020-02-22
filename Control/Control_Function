import numpy as np

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