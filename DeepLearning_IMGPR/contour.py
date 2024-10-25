import cv2

img = cv2.imread('3.jpg', 0)

# 127 is threshhold value(variable) and 255 is max value assigned to threshhold , thresh_binary(convert image to binary )

_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()