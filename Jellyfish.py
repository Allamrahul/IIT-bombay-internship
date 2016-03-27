import cv2
import numpy as np#import numpy array for fast array manipulations
img=cv2.imread("jellyfish.jpg")#reading the image
frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#RGB color space to HSV
mask = cv2.inRange(frame,np.array([120, 80, 80]),np.array([140, 255, 255]))#separating out purple
res = cv2.bitwise_and(img,img, mask= mask)#Equivalent to multiplying the image with mask
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)#RGB to gray
blurred = cv2.GaussianBlur(gray, (5, 5), 0)#removing noise by averaging
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]#As good as saying if a pixel falls into the range 1 is assigned,else 0
mask = cv2.erode(thresh, None, iterations=2)#eroding
mask = cv2.dilate(mask, None, iterations=2)#dilating
contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2:]#finding contours
for c in contours:#looping through all the contours
    area=cv2.contourArea(c)#finding contour area
    if area >40:
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])#finding centroid of contours
		cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
		cv2.putText(img, "x", (cX, cY),#displaying  "x"
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)#For varying the properties of "x"
cv2.imshow("Image", img)#output the image
cv2.waitKey(0)
cv2.destroyAllWindows()
