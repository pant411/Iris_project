import cv2 as cv
import numpy as np
import os


img = cv.imread("test.jpg")

upper = np.array([135,150,150],np.uint8)
lower = np.array([0,0,0],np.uint8)
result = cv.inRange(img,lower,upper)

result = cv.bitwise_not(result)
result  = cv.cvtColor(result , cv.COLOR_GRAY2BGR)


cv.imwrite("result2.jpg", result)

