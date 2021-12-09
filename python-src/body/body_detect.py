"""
Sources:
    https://pjreddie.com/darknet/yolo/
    https://www.youtube.com/watch?v=1LCb1PVqzeY
"""

import cv2
import numpy as np
import os

class Body_detect:

    def __init__(self):
        """Infrastructure for body detection using yolov3."""

        self.CLASS_FOLDER = os.path.dirname(__file__)
        self.net = cv2.dnn.readNet(self.CLASS_FOLDER + '/yolov3-tiny.weights', self.CLASS_FOLDER + '/yolov3-tiny.cfg')
        self.image = cv2.imread(self.CLASS_FOLDER + '/test.jpg')

        self.boxes = []
        self.confidences = []
        self.indexes = []

        print('Instantiated body detection class')

    def set_image(self, frame):
        """Sets image to input frame."""
        self.image = frame

    def find_bodies(self):
        """Identifies bodies in image using yolo model.

        Returns:
            (list): contains the coordinates of each detected body
        """
        self.reset()

        # Format image
        height, width, _ = self.image.shape
        blob = cv2.dnn.blobFromImage(self.image, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)

        # Input image into the yolo model and extract the output layers
        self.net.setInput(blob)
        output_layers_names = self.net.getUnconnectedOutLayersNames()
        layerOutputs = self.net.forward(output_layers_names)

        # Get information about each identified body
        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores) # Determine highest class prediction
                confidence = scores[class_id]
                if confidence > 0.5: # If body is accurately detected, extract bounding box information
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    self.boxes.append([x, y, w, h])
                    self.confidences.append((float(confidence)))

        # Apply non-maxima suppression to filter the bounding boxes
        self.indexes = cv2.dnn.NMSBoxes(self.boxes, self.confidences, 0.5, 0.4)

        # Extract coordinates of each body's bounding box and visualize box
        bodies = []
        if len(self.indexes) > 0:
            for i in self.indexes.flatten():
                x, y, w, h = self.boxes[i]
                bodies.append([x, y])
                cv2.rectangle(self.image, (x,y), (x+w, y+h), (255,0,0), 2)

        return bodies, self.image

    def reset(self):
        """Clear lists that contain boxes, confidences, and indexes."""

        self.boxes = []
        self.confidences = []
        self.indexes = []
