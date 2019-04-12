from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 

camera = PiCamera() #initialize RPI camera module
camera.resolution = (640, 480) #set image resolution
#camera.shutter_speed = 100 #uncomment if doing actual analysis of led's
camera.framerate = 60 #doesnt make much of a difference with this
rawCapture = PiRGBArray(camera, size=(640, 480)) #captures footage from RPI camera as an array
count = 0
t = time.time() # start timer

time.sleep(0.1) #waits for camera to turn on

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): #capture is continous as long as camera is running
	image = frame.array #converts captured array to an image
	#cv2.imshow("response", image) #not showing images saves ~1 sec of total capturing time
	cv2.imwrite("pictures/frame" + str(count) + ".jpg", image) # not saving images saves ~3 secs of total capturing time
	#key = cv2.waitKey(1) & 0xFF #only use if video stream is continous
	rawCapture.truncate(0) #converts rawCapture array back to an array of zeros to prevent data overlaps
	count += 1
	#done = time.time() - t	
	if (count == 100): #breaks loop after 100 images created
		break
	#if key == ord("q"): #use this only if the video is continuous
		#break
camera.close()
done = time.time() - t #prints time taken for code to run
print('time taken: ' + str(done))
