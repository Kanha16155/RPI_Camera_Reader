import cv2
import numpy

count = 0
while (count < 100): #100 images coming from cameraRUN.py
	img = cv2.imread("pictures/frame"+str(count)+".jpg", flags=cv2.IMREAD_COLOR) #reads image from file
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #converts pixel values from RGB to HSV
	lower_red = numpy.array([0,50,50]) #sets lower hue value to be read
	upper_red = numpy.array([10,255,255]) #sets highest value to be red
	mask = cv2.inRange(hsv, lower_red, upper_red) #creates a mask which shows the pixels that fall into the upper and lower bounds
	res = cv2.bitwise_and(img,img, mask = mask) #and operation with image and mask created
	cv2.imshow('frame',img) 
	cv2.imshow('mask',mask) 
	cv2.imshow('res',res)
	k = cv2.waitKey(1) & 0xFF 
	#key = cv2.waitKey(1) & 0xFF
	if k == ord("q"): #pressing 'q' increments the images shown
		count += 1
	#if key == ord("r"): #does not work well
		#break
cv2.destroyAllWindows() #closes all open windows after all images are read
