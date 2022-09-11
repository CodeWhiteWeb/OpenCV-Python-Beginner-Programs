# Drawing a Rectangle
# It takes in 5 arguments –
# Image
# Top-left corner co-ordinates
# Bottom-right corner co-ordinates
# Color (in BGR format)
# Line width

import cv2 # import the library
image=cv2.imread("resources\small.jpg")
output = image.copy()# Copying the original image
rectangle = cv2.rectangle(output, (200, 400), (600, 800), (255, 0, 0), 2)# Using the rectangle() function to create a rectangle.
cv2.imshow("Rectangle is ",rectangle)