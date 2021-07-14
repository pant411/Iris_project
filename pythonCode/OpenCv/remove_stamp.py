import cv2 
import numpy as np
import os

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

dir_path = 'Doc\\'
fileList = createFileList(dir_path)

for files in fileList:
    print(files)
    img = cv2.imread(files)

    upper = np.array([135,150,150],np.uint8)
    lower = np.array([0,0,0],np.uint8)
    result = cv2.inRange(img,lower,upper)

    result = cv2.bitwise_not(result)
    result  = cv2.cvtColor(result , cv2.COLOR_GRAY2BGR)

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 4:
            cv2.drawContours(thresh, [c], -1, (0,0,0), -1)
            
    result = cv2.bitwise_not(thresh)
    name = files[4:]
    cv2.imwrite('remove_stamp_doc\\{}'.format(name), result)

