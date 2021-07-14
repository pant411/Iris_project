import numpy as np
import cv2

'''img = cv2.imread("d3.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.multiply(img, 1.2)
kernel = np.ones((1, 1), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
cv2.imwrite("input.jpg", img)'''
img = cv2.imread("5.jpg")
print("get it")
img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21) 
img = cv2.resize(img, (1240,1754), interpolation = cv2.INTER_AREA)
height,width ,channel= img.shape
cv2.imwrite("newimg.jpg", img)
print('start')
for x in range(height):
    for y in range(width):
        color = img[x,y]
        if not (color[0] == color[1] == color[2]):
            img[x,y] = [255,255,255]
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(grayimg,113,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imwrite('newimg1.jpg', th1)
cv2.imwrite('newimg2.jpg', th2)
cv2.imwrite('newimg3.jpg', th3)
cv2.imwrite('newimg4.jpg', grayimg)
print('finish')

