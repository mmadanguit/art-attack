# import the necessary packages
from imutils.video import VideoStream
import imutils
import cv2
import time
import numpy as np

vs = VideoStream(src=0).start()
time.sleep(1)

firstFrame = None

while True:
    # Grab the frame from the threaded video stream
    frame = vs.read()

    # Resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # If the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        print("First frame set")
        continue

    # Compute the absolute difference between the current frame and first frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # Filter out frames where person is too close
    s = set(thresh[0])
    print(thresh, s)
    # if s == {255}:
    #     print('True')
    #     continue

    # Dilate the thresholded image to fill in holes, then find contours on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Loop over the contours
    for c in cnts:
        # If the contour is too small, ignore it
        if cv2.contourArea(c) < 500:
            continue

        # Compute the bounding box for the contour and draw it on the frame
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    cv2.imshow("First Frame", firstFrame)

    key = cv2.waitKey(1) & 0xFF

    # Break from the loop if the `q` key is pressed
    if key == ord("q"):
    	break

# Cleanup the camera and close any windows
cv2.destroyAllWindows()
vs.stop()
