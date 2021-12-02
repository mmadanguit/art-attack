"""
Sources:
    https://pjreddie.com/darknet/yolo/
    https://www.youtube.com/watch?v=1LCb1PVqzeY
"""

import cv2
import numpy as np

class Body_detect:

    def __init__(self):
        """Infrastructure for body detection using yolov3."""

        self.net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')
        self.image = cv2.imread('test.jpg')

        self.boxes = []
        self.confidences = []
        self.indexes = []

        print('Instantiated body detection class')

    def capture(self):
        """Sets image to frame from camera."""
        cap = cv2.VideoCapture(0)
        _, self.image = cap.read()

        print("Image captured")

    def find_bodies(self):
        """Identifies bodies in image using yolo model.

        Returns:
            (list): contains the coordinates of each detected body
        """

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

        # Extract coordinates of each body's bounding box
        bodies = []
        if len(self.indexes) > 0:
            for i in self.indexes.flatten():
                x, y, w, h = self.boxes[i]
                bodies.append([x, y])

        print(bodies)
        return bodies

    def visualize(self):
        """Visualizes bounding boxes and saves the resulting image."""

        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(self.boxes), 3))
        if len(self.indexes) > 0:
            for i in self.indexes.flatten():
                x, y, w, h = self.boxes[i]
                label = "person"
                confidence = str(round(self.confidences[i], 2))
                color = colors[i]
                cv2.rectangle(self.image, (x,y), (x+w, y+h), color, 2)
                cv2.putText(self.image, str(x) + " " + str(y) + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 2)

        cv2.imwrite('output.jpg', self.image)
        print("Image saved")
