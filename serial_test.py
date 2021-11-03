# Sources:
# https://sd2020spring.github.io/toolboxes/image-processing
# https://github.com/Db1998/Facial-Distance

import numpy as np
import cv2
import serial
import time
import math

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# Instantiate face detector from OpenCV library
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

def send_position(face_box):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))
        # Calculates facial distance from camera in real-time
        # Distance = (No. of pixels in the width of face image) * (Width of the face) / (focal length)
        dst = 6421 / w
        dst = '%.2f' % dst
    # use a sigmoid function to make the distance between 0 and 1
    squish_dst = 1 / (1 + math.exp(-dst))
    # send a servo position to arduino based on the face distance
    arduino.write(bytes(int(180 * squish_dst), 'utf-8'))
    time.sleep(0.05)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Run face detector to get a list of faces in the image
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))

    send_position(faces)

    # Draw a red box around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))
        # Calculates facial distance from camera in real-time
        # Distance = (No. of pixels in the width of face image) * (Width of the face) / (focal length)
        dst = 6421 / w
        dst = '%.2f' % dst
        # Displays facial distance
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(dst), (x, y-10), font, 1, (0, 50, 250), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()