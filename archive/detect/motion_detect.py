"""
Sources:
    https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
"""

import cv2
import numpy as np

class Motion_detect:

    def __init__(self):
        """Infrastructure for body detection using yolov3."""

        self.firstFrame = None

    def calibrate(self, frame):
        """Initialize first frame"""
        self.firstFrame = frame
