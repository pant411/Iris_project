#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

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

dir_path = 'D:\\iris_project\\massure\\Doc\\jpg'
fileList = createFileList(dir_path)
length = len(dir_path)
for files in fileList:
    print(files)
    name = files[length:]
    txtname = name[:-4]
    img = cv2.imread(files)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (80, 20))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)


    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    im2 = img.copy()

    file = open("D:\\iris_project\\massure\\Doc\\resultxt1\\{}.txt".format(txtname), "w+",encoding ="utf-8")
    file.write("")
    file.close()

    contours.reverse()

    custom_config = r'--oem 1 -l tha+eng --psm 6'

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 7880:
            x, y, w, h = cv2.boundingRect(cnt)
            
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            cropped = im2[y:y + h, x:x + w]
            
            file = open("D:\\iris_project\\massure\\Doc\\resultxt1\\{}.txt".format(txtname), "a",encoding ="utf-8")
            
            text = pytesseract.image_to_string(cropped,config=custom_config)
            
            #print(text)
            file.write(text)
            
            file.close
            
    cv2.imwrite("D:\\iris_project\\Crop_image\\{}".format(name),im2)
