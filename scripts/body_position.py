"""
Sources:
https://medium.com/instrument-stories/body-detection-with-computer-vision-1898cdc6b7d
https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/
"""
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
# import serial_cmd

# Instantiate serial command
# control = serial_cmd.Serial_cmd()

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the image to reduce detection time and improve detection accuracy
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))
    orig = frame.copy()

    # Run person detector in the image
    (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# Apply non-maxima suppression to the bounding boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65) # Use a fairly large overlap threshold to try to maintain overlapping boxes that are still people

	# Draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
