from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy as np
import cv2 
import matplotlib.pyplot as plt
import argparse
import os
import shutil
import sys





img = cv2.imread('input.jpg')
#img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21) 
#img = cv2.resize(img, (1240,1754), interpolation = cv2.INTER_AREA)
# define the list of boundaries
boundaries = [
        ([0, 0,0], [255, 255, 255]),
	([63, 60,99], [95, 94, 136]),
	([150, 69, 31], [189, 100, 65]),
        ([254, 254, 254], [254, 254, 254])
]
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(img, lower, upper)
	output = cv2.bitwise_and(img, img, mask = mask)
	# show the images
	#cv2.imshow('image',mask)
	cv2.imshow('image',output)
	#cv2.imshow("images", np.hstack([img, output]))
	cv2.waitKey(0)
	

