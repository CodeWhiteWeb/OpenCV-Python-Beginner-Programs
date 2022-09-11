# Image Cropping
import cv2 # OpenCV
img=cv2.imread("resources\small.jpg") # Read image
print(img.shape) # Print image shape
imgResize = cv2.resize(img,(300,200)) # Resize image
print(imgResize.shape) # Print image shape
imgCrop = img[0:200,200:500] # Crop image
cv2.imshow("Image",img) # Display image
cv2.imshow("Rezie Image",imgResize) # Display resized image
cv2.imshow("Cropped Image",imgCrop) # Display cropped image
cv2.waitKey(0)