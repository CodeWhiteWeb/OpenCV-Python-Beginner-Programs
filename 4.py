# Extracting the Region of Interest (ROI)

import cv2 # OpenCV
image = cv2.imread('resources\small.jpg') # Read image
roi = image[100 : 500, 200 : 700] # Extract ROI
cv2.imshow("Region of Interest is ",roi) # Display ROI