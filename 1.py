# Reading an image
import cv2 # OpenCV
print("Package Imported") # Print message
img=cv2.imread("resources\small.jpg") # Read image
cv2.imshow("Output",img) # Display image
cv2.waitKey(0) # Wait for any key to be pressed