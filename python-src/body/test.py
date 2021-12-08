# import the necessary packages
import video_stream
import body_detect
import imutils
import cv2

vs = video_stream.Video_stream().start()
body = body_detect.Body_detect()

while True:
	# Grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    body.set_image(frame)
    coord, frame = body.find_bodies()
    print(coord)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()


# while True:
#     # Find body position from camera feed
#     body.capture()
#     body.visualize()
#     if len(body.find_bodies()) > 0:
#         xy = body.find_bodies()[0]
#         print("bodies", xy)
#
#     body.reset()
