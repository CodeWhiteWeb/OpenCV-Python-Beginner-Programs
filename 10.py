# Rotate an Image
import cv2  # OpenCV
image = cv2.imread('resources\small.jpg') # Read image
h, w = image.shape[:2] # Get image height and width
center = (w // 2, h // 2) # Get center of image
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)  # Calculating the rotation matrix
rotated = cv2.warpAffine(image, matrix, (w, h)) # Rotating the image
cv2.imshow("Rotated Image ",rotated) # Displaying the image