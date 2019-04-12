from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 

camera = PiCamera()
camera.resolution = (640, 480)
#camera.shutter_speed = 100
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))
count = 0
t = time.time()

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	#cv2.imshow("response", image)
	cv2.imwrite("pictures/frame" + str(count) + ".jpg", image)
	
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	count +=1
	#done = time.time() - t
	
	if (count == 100):
		break
	#if key == ord("q"):
		#break
camera.close()
done = time.time() - t
print('time taken: ' + str(done))
