import body_detect
import time

detect = body_detect.Body_detect()
time.sleep(1.65)

while True:
    detect.capture()
    detect.find_bodies()
