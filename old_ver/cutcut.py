import cv2 
import numpy as np  

img = cv2.imread('close.jpg')
height,width ,channel= img.shape
min = [255,255,255]
max = [0,0,0]
res = []
count = 1 
for x in range(height):
    for y in range(width):
        print ('{} pixel'.format(count),end='')
        color = img[x,y]
        if color[2] != color[1] != color[0]:
            res.append(color)
        print (' Red = ',color[2],end='')
        print (' Green = ',color[1],end='')
        print (' Blue = ',color[0],end='')
        print()
        if (min[2] > color[2]):
            min[2] = color[2]
        if (min[1] > color[1]):
            min[1] = color[1]
        if (min[0] > color[0]):
            min[0] = color[0]
        if (max[2] < color[2]):
            max[2] = color[2]
        if (max[1] < color[1]):
            max[1] = color[1]
        if (max[0] < color[0]):
            max[0] = color[0]  
        count += 1
print('min red = {} min green = {} min blue = {}'.format(min[2],min[1],min[0]))
print('max red = {} max green = {} max blue = {}'.format(max[2],max[1],max[0]))



lower = np.array([min[0],min[1],min[2]])
upper = np.array([max[0],max[1],max[2]])
print(lower)
print(upper)
print(res)
