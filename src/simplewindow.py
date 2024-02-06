#!/home/underw23/anaconda3/bin/python3
import cv2 as cv
import sys
import numpy as np


image = cv.imread(cv.samples.findFile('../images/connor_boba.jpg'))

if image is None:
	print("cant read image")
	
image = cv.resize(image, (960, 540))


cv.imshow("Display window", image)


# 0 means wait indefinitely

k = cv.waitKey(0)

if k == ord("s"):
	cv.imwrite("../images/connor_boba.jpg", image)
