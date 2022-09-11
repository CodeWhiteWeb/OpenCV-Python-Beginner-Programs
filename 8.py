#Convert an Image to Blur Image
import cv2 # OpenCV
img=cv2.imread("resources\small.jpg") # Read image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert to gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # Blur image
cv2.imshow("Gray Image",imgGray) # Display gray image
cv2.imshow("Blur Image",imgBlur) # Display blur image
cv2.waitKey(0)
