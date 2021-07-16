#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytesseract
import os
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 1 -l tha --psm 6'

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

floder = ["gauss","s&p","poisson","normal"]
for dirr in floder:
    dir_path = 'D:\\iris_project\\massure\\list_name\\pic\\{}\\'.format(dirr)
    fileList = createFileList(dir_path)
    length = len(dir_path)

    file = open("D:\\iris_project\\massure\\list_name\\text\\{}\\result_{}.txt".format(dirr,dirr), "w+",encoding ="utf-8")
    file.write("")
    file.close()
    
    for files in fileList:
        print(files)

        img = cv2.imread(files)
    
        file = open("D:\\iris_project\\massure\\list_name\\text\\{}\\result_{}.txt".format(dirr,dirr), "a",encoding ="utf-8")            
        text = pytesseract.image_to_string(img,config=custom_config)
            
        #print(text)
        file.write(text)
        file.close
        
