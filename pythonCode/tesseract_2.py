#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import pytesseract
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 1 -l tha+eng --psm 6'

def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    fileList.sort()
    return fileList

def deskew(im, max_skew=10):
    height, width = im.shape

    # Create a grayscale image and denoise it
    #im_gs = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gs = im
    im_gs = cv2.fastNlMeansDenoising(im_gs, h=3)

    # Create an inverted B&W copy using Otsu (automatic) thresholding
    im_bw = cv2.threshold(im_gs, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Detect lines in this image. Parameters here mostly arrived at by trial and error.
    lines = cv2.HoughLinesP(
        im_bw, 1, np.pi / 180, 200, minLineLength=width / 12, maxLineGap=width / 150
    )

    # Collect the angles of these lines (in radians)
    angles = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angles.append(np.arctan2(y2 - y1, x2 - x1))

    # If the majority of our lines are vertical, this is probably a landscape image
    landscape = np.sum([abs(angle) > np.pi / 4 for angle in angles]) > len(angles) / 2

    # Filter the angles to remove outliers based on max_skew
    if landscape:
        angles = [
            angle
            for angle in angles
            if np.deg2rad(90 - max_skew) < abs(angle) < np.deg2rad(90 + max_skew)
        ]
    else:
        angles = [angle for angle in angles if abs(angle) < np.deg2rad(max_skew)]

    if len(angles) < 5:
        # Insufficient data to deskew
        return im

    # Average the angles to a degree offset
    angle_deg = np.rad2deg(np.median(angles))

    # If this is landscape image, rotate the entire canvas appropriately
    if landscape:
        if angle_deg < 0:
            im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
            angle_deg += 90
        elif angle_deg > 0:
            im = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)
            angle_deg -= 90

    # Rotate the image by the residual offset
    M = cv2.getRotationMatrix2D((width / 2, height / 2), angle_deg, 1)
    im = cv2.warpAffine(im, M, (width, height), borderMode=cv2.BORDER_REPLICATE)
    return im

dir_path = 'D:\\iris_project\\massure\\Doc\\jpg'
fileList = createFileList(dir_path)
length = len(dir_path)
for files in fileList:
    print(files)
    name = files[length:]
    txtname = name[:-4]

    img = cv2.imread(files, cv2.IMREAD_GRAYSCALE)
    img = cv2.multiply(img, 1.2)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    
    img = deskew(img)
    img = cv2.fastNlMeansDenoising(img,None,10,7,21)
    img = cv2.resize(img, (1240,1754), interpolation = cv2.INTER_AREA)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    
    
    file = open("D:\\iris_project\\massure\\Doc\\resultxt2\\{}.txt".format(txtname), "w+",encoding ="utf-8")
    file.write("")
    file.close()
     
    file = open("D:\\iris_project\\massure\\Doc\\resultxt2\\{}.txt".format(txtname), "a",encoding ="utf-8")
            
    text = pytesseract.image_to_string(img,config=custom_config)
    #print(text)
    file.write(text)
    file.close
            
