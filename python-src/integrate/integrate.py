import cv2
import numpy as np
import serial_cmd
import body_detect
import motor_ctrl

# Instantiate serial command
control = serial_cmd.Serial_cmd()

# Instantiate motor control
motor = motor_ctrl.Motor_ctrl()

# Instantiate body detection
body = body_detect.Body_detect()

while True:
    # Find body position from camera feed
    body.capture()
    if len(body.find_bodies()) > 0:
        xy = body.find_bodies()[0]

        # Set body position in motor class
        motor.set_xy(xy[0], xy[1])

        # Use follow method to position motors in front of body
        motor.motor_target()
        motor.follow()

        # Set each servo
        for i in range(motor.num_motors):
            print(motor.num_position(i))
            num, pos = motor.num_position(i)
            control.set_servo(num, pos)
