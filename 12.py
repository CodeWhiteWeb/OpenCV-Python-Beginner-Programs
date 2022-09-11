#Displaying text on Image
# It takes in 7 arguments –
# Image
# Text to be displayed
# Bottom-left corner co-ordinates, from where the text should start
# Font
# Font size
# Color (BGR format)
# Line width

import cv2 # import the library
image=cv2.imread("resources\small.jpg")
output = image.copy() # Copying the original image
text = cv2.putText(output, 'OpenCV Demo', (500, 550),cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 0), 2) # Adding the text using putText() function
cv2.imshow("Coding Image",text) # show the image