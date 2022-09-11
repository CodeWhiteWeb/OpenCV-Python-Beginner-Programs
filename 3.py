# Extracting the RGB values of a pixel
# Note – OpenCV arranges the channels in BGR order. So the 0th value will correspond to Blue pixel and not Red.
import cv2 # OpenCV
image = cv2.imread('resources\small.jpg') # Read image
(B, G, R) = image[100, 100] # Extract RGB values
print("R = {}, G = {}, B = {}".format(R, G, B)) # Print RGB values

# We can also pass the channel to extract the value for a specific channel
B = image[100, 100, 0] # Extract Blue value
G = image[100, 100, 1] # Extract Green value
R = image[100, 100, 2] # Extract Red value
print(" B = {}".format(B)) # Print Blue value
print(" G = {}".format(G)) # Print Green value
print(" R = {}".format(R)) # Print Red value