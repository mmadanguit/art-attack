import cv2
import numpy as np
import time
import imutils
import serial.serial_cmd as serial_cmd
import body.body_detect as body_detect
import motor.motor_ctrl as motor_ctrl
import body.video_stream as video_stream

# Instantiate serial command
control = serial_cmd.Serial_cmd()

time.sleep(1.65)

# Instantiate motor control
motor = motor_ctrl.Motor_ctrl()

vs = video_stream.Video_stream().start()

# Instantiate body detection
body = body_detect.Body_detect()

mod_iterator = 0

while True:
    # Grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    body.set_image(frame)
    coord, frame = body.find_bodies()

    # Display the resulting image
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    # If a body is found, make the motors stick out in a column in front of the person
    if len(coord) > 0:
        coord = coord[0]
        print("bodies", coord)

        # Set body position in motor class
        motor.set_xy(coord[0], coord[1])

        # Use follow method to position motors in front of body
        motor.motor_target()
        motor.column_follow()

        # Set each servo
        for i in range(motor.num_motors):
            num, pos = motor.num_position(i)
            control.set_servo(num, pos)

        time.sleep(0.05)

    # If a body is not found, move the motors in a wave
    else:
        motor.wave_column(mod_iterator)
        mod_iterator += 1
        # Set each servo
        for i in range(motor.num_motors):
            num, pos = motor.num_position(i)
            control.set_servo(num, pos)

        time.sleep(0.05)
