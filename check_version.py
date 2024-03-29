# 15 Oct 2019
# Joel Godinez
# python check_version.py


# import the necessary packages
from __future__ import print_function
import imutils
import cv2
import timeit
import time
import numpy as np


# start timing execution time
start_time = time.time()
# load the Tetris block image, convert it to grayscale, and threshold
# the image
print("OpenCV Version: {}".format(cv2.__version__))
image = cv2.imread("tetris_blocks.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

# check to see if we are using OpenCV 2.X
if imutils.is_cv2() or imutils.is_cv4():
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

# check to see if we are using OpenCV 3
elif imutils.is_cv3():
	(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

# draw the contours on the image
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Image", image)
print("--- %s seconds ---" % (time.time() - start_time))
cv2.waitKey(0)

