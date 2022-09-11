#Convert RGB Image to GrayScale Image
import cv2 # OpenCV
img = cv2.imread('butterfly.jpg') # Read image
print(img.shape) # Print image shape
cv2.imshow('Original', img) # Display image
cv2.waitKey(1) ## Wait for 1 millisecond
#Use cvtColor, to convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to gray
print(gray_img.shape) # Print image shape
cv2.imshow('Grayscale', gray_img) # Display image
cv2.waitKey(0)