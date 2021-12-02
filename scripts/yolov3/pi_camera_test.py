"""
Sources:
https://pjreddie.com/darknet/yolo/
https://www.youtube.com/watch?v=1LCb1PVqzeY
"""
import cv2
import numpy as np
import serial_cmd
import motor_control
import time

# Instantiate serial command
control = serial_cmd.Serial_cmd()

# Instantiate motor control
motor = motor_control.Motor_control()

# Load yolo weights and configuration files
net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')

# cap = cv2.VideoCapture(0)
# ret,frame = cap.read() # return a single frame in variable `frame`

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')


while(True):
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)
    cv2.imshow('img1',image) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()

while True:
    # Capture frame-by-frame
    _, image = cap.read()
    height, width, _ = image.shape

    blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    # Get information from each identified object
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                print(x, y)
                motor.set_xy(x, y)
                motor.motor_target()
                print(motor.target_motor)
                motor.wave_column()
                for i in range(motor.num_motors):
                    print(motor.num_position(i))
                    num, pos = motor.num_position(i)
                    control.set_servo(num, pos)
                time.sleep(.5)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

	# Apply non-maxima suppression to the bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = "person"
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(image, (x,y), (x+w, y+h), color, 2)
            cv2.putText(image, label + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 2)

    # Display the resulting image
    cv2.imshow('Image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
