from imutils.video import WebcamVideoStream
import imutils
import cv2
import numpy as np

net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')
vs = WebcamVideoStream().start()

# Load yolo weights and configuration files
net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')

cap = cv2.VideoCapture(0)

while True:
    image = vs.read()
    print("New image")

    blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []

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

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))

	# Apply non-maxima suppression to the bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # font = cv2.FONT_HERSHEY_PLAIN
    # colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            print(x, y)
    #         label = "person"
    #         confidence = str(round(confidences[i], 2))
    #         color = colors[i]
    #         cv2.rectangle(image, (x,y), (x+w, y+h), color, 2)
    #         cv2.putText(image, str(x) + " " + str(y) + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 2)
    #
    # Display the resulting image
    # cv2.imshow('Image', image)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
