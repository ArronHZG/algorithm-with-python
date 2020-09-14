import cv2

img = cv2.imread('echo.jpg')
print(img)
img = cv2.resize(img, (256, 341))
cv2.imwrite('../echo-1.jpg', img)
