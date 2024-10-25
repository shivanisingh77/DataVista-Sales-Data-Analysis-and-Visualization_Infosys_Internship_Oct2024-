import os
import cv2

# Path of the image
image_path = '1.jpg'

# to Read the image
image = cv2.imread(image_path)

# to display the image using OpenCV

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print("Image dimensions:", image.shape)
