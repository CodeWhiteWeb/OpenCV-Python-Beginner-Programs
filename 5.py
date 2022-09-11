# Image Resizing

import cv2 # OpenCV
img=cv2.imread("resources\small.jpg") # Read image
print(img.shape) # Print image shape
imgResize = cv2.resize(img,(500,400)) # Resize image
print(imgResize.shape) # Print image shape
cv2.imshow("Image",img) # Display image
cv2.imshow("Resized Image",imgResize) # Display resized image
cv2.waitKey(0)