"""
Sources:
    https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
"""

from threading import Thread
import cv2

class Video_stream:

    def __init__(self):
    	# Initializes the video camera stream and read the first frame from the stream
    	self.stream = cv2.VideoCapture(0)
    	(self.grabbed, self.frame) = self.stream.read()
    	# Initializes the variable used to indicate if the thread should be stopped
    	self.stopped = False

    def start(self):
        """Starts the thread to read frames from the video stream."""
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
    	"""Reads next frame from the stream infinitely until the thread is stopped"""
    	while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
    	"""Returns the frame most recently read"""
    	return self.frame

    def stop(self):
    	"""Indicate that the thread should be stopped"""
    	self.stopped = True
