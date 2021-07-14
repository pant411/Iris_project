import cv2

# Load image, convert to grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('result2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Filter using contour area and remove small noise
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < 4:
        cv2.drawContours(thresh, [c], -1, (0,0,0), -1)


close = cv2.bitwise_not(thresh)

cv2.imwrite('thresh.jpg', thresh)
cv2.imwrite('close.jpg', close)
cv2.waitKey()
