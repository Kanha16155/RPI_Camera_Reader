import cv2
import numpy
count = 0
while (count < 100):
	img = cv2.imread("pictures/frame"+str(count)+".jpg", flags=cv2.IMREAD_COLOR)	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
	lower_red = numpy.array([0,50,50]) 
	upper_red = numpy.array([10,255,255]) 
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(img,img, mask= mask) 
	cv2.imshow('frame',img) 
	cv2.imshow('mask',mask) 
	cv2.imshow('res',res)
	k = cv2.waitKey(1) & 0xFF
	key = cv2.waitKey(1) & 0xFF
	if k == ord("q"): 
		count +=1
	#if key == ord("r"):
		#break
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 

 
