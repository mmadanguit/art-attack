---
title: 'Software and Firmware Subsystems'
description: Learn more about our python package and how we interfaced between Python and Arduino. 
image: './../images/textile.jpeg'
---

## Python Classes
Our python package to control our interactive sculpture consists of three classes. The first class uses camera data to track and report the position of people in front of the sculpture. The second class translates that body position into a position for each motor. The last class takes the position of each motor and facilitates serial communication to the Arduino.

### Body Detection
The [body detection class](https://github.com/mmadanguit/art-attack/blob/main/python-src/body/body_detect.py) handles person detection from the camera’s raw video feed. Its `find_bodies` method returns a list of the (x, y) coordinates of all the detected bodies in the frame and the frame with bounding boxes around each body. We experimented with three different body finding algorithms: [OpenCV face detection with Haar Cascades](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html), [YOLO-COCO body detection](https://pjreddie.com/darknet/yolo/), and [OpenCV motion detection using background segmentation](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/). We ultimately chose to use the YOLO-COCO body detection algorithm due to its reliability and speed. The YOLO-COCO body detection algorithm works by breaking an image down into an array of variously sized pieces (called a blob) and treats each with a weights file to detect a wide range of objects, one of which can be a person. The YOLO-COCO body detection was reliable in the sense that it was able to detect people regardless of whether or not they were wearing a mask. We were also able to minimize computation time by using the smallest set of weights and sacrificing some detection ability. In the future, we would probably switch to a version of YOLO-COCO that is specific to person detection to reduce computational load.

To further reduce computational load, we moved the reading of frames from the camera to a completely separate thread. Doing so allowed us to continuously read from the webcam while the current frame was being processed. So, instead of having to wait to read from the webcam to process the frame, the main thread can simply grab the current frame from the background camera thread. 

### Motor Control
The [motor control class](https://github.com/mmadanguit/art-attack/blob/main/python-src/motor/motor_ctrl.py) uses the body positions found using the body detect class in order to assign positions for each motor. The class is able to use the (x, y) position to first assign which motor is most directly in front of the person. From there, two main methods can be used. The `follow` method follows the person's movements in front of the sculpture by protruding a spot on the textile in front of the person. The `column_follow` method follows the person’s movements by protruding an entire column of the textile in front of them. Additionally, there is a `wave_column` method that facilitates the movement of the sculpture in a wave pattern that does not consider the position of people in front of it. The position of any motor can be found by calling the `num_position` method with the motor number (0-15). This method returns the motor number and motor position as strings ready to send to the Arduino through serial communication. 

### Serial Communication
The [serial communication class](https://github.com/mmadanguit/art-attack/blob/main/python-src/comms/serial_cmd.py) is responsible for sending motor commands to the Arduino. Since we decided to do the majority of the processing work in Python, the Arduino acts solely as a bridge between Python and the motors. 

There are two ways that we could have sent motor commands over to the Arduino. We could either send all 16 motor positions over at once in the form of a list, or we could send individual motor positions. If we were to send all 16 motor positions over at once, we would be sending a string with 48 characters (3 for each motor position) plus 15 characters (for each comma separating each motor position) plus 2 additional characters (for the start and end of message markers), yielding a total of 49 characters. If we were to send individual motor positions, we would be sending a string with 6 characters (2 of which represent the motor to be commanded, 3 of which the motor position, and 1 of which represents the comma separating the two) plus 2 additional characters (for the start and end of message markers), yielding a total of 8 characters. We ultimately decided that since we will not be moving more than 4 motors at a time, it would make the most sense to send individual motor commands. If we were to consider a movement algorithm that moves more than 4 motors at a single time, we might want to reconsider how we are sending over our motor messages. We could have also considered converted our messages to hex to further reduce message size and computational load.

When you initialize an instance of the serial communication class, the Python code connects to the Serial port. Once it has connected, we can use the set_servo method to set individual servo positions by providing the relevant servo number and the position to set the servo to. The method formats the string correctly with our decided start and end message characters and sends it over the Serial port to be read by the Arduino. 

## Python Virtual Environment
We set up a Python virtual environment which automatically downloads all required dependencies. These dependencies are numpy, pyserial, OpenCV, and imutils. Python version 3.6 or greater is also needed. To use the virtual environment run the following commands:
```
sudo apt update
source setup-python-venv.sh
```

## Arduino Code
The [Arduino code](https://github.com/mmadanguit/art-attack/blob/main/arduino-src/serial-cmd/serial-cmd.ino) takes in motor commands from our Python script and moves the motors. We are using an PCA9685 16-Channel Servo Driver from Adafruit, and connecting the Arduino using the I2C bus. We are using the [Adafruit PWM Servo Driver Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library) for the servo driver. 

In the `void` loop, we are constantly checking for messages on the Serial port. If a new message has been received, our `parseCommand` function will read the motor command and set the given servo to the servo position.

## Link to the GitHub
Here's a link to [our GitHub repository](https://github.com/mmadanguit/art-attack).
