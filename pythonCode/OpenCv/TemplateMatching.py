import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

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

dir_path = 'D:\\iris_project\\Doc\\'
fileList = createFileList(dir_path)

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for files in fileList:
    name = files[4:]
    img1 = cv.imread(cv.samples.findFile(files),0)
    img2 = img1.copy()
    img3 = cv.imread(files)
    img4 = img3.copy()
    template1 = cv.imread('D:\\iris_project\\logo\\logo1.jpg',0)
    template2 = cv.imread('D:\\iris_project\\logo\\logo2.jpg',0)
    template3 = cv.imread('D:\\iris_project\\logo\\logo3.jpg',0)
    template4 = cv.imread('D:\\iris_project\\logo\\logo4.jpg',0)
    template5 = cv.imread('D:\\iris_project\\logo\\logo5.jpg',0)
    w1, h1 = template1.shape
    w2, h2 = template2.shape
    w3, h3 = template3.shape
    w4, h4 = template4.shape
    w5, h5 = template5.shape

    for meth in methods:
        img1 = img2.copy()
        img3 = img4.copy()
        method = eval(meth)

        res = cv.matchTemplate(img1,template1,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + h1, top_left[1] + w1)
        cv.rectangle(img3,top_left, bottom_right, (255,0,0),2)

        res = cv.matchTemplate(img1,template2,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + h2, top_left[1] + w2)
        cv.rectangle(img3,top_left, bottom_right, (0,255,0),2)

        res = cv.matchTemplate(img1,template3,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + h3, top_left[1] + w3)
        cv.rectangle(img3,top_left, bottom_right, (0,0,255),2)

        res = cv.matchTemplate(img1,template4,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + h4, top_left[1] + w4)
        cv.rectangle(img3,top_left, bottom_right, (255,0,255),2)

        res = cv.matchTemplate(img1,template5,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + h5, top_left[1] + w5)
        cv.rectangle(img3,top_left, bottom_right, (0,255,255),2)


        cv.imwrite('D:\\iris_project\\result\\{}\\template_result_{}.jpg'.format(meth,name),img3)

