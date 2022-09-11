#Convert an Image to Canny Image
#Edge Detection is performed using Canny Edge Detection which is a multi-stage algorithm.
import cv2 # OpenCV
img=cv2.imread("resources\small.jpg") # Read image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert to gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # Blur image
imgCanny = cv2.Canny(img,50,50) # Canny image
cv2.imshow("Gray Image",imgGray) # Display gray image
cv2.imshow("Blur Image",imgBlur) # Display blur image
cv2.imshow("Canny Image",imgCanny) # Display canny image
cv2.waitKey(0)
