# Extracting the height and width of an image
import cv2 # OpenCV
image = cv2.imread('resources\small.jpg') # Read image
h, w = image.shape[:2] # Get image height and width
print("Height = {}, Width = {}".format(h, w)) # Print image height and width