#Read Video
import cv2 # import the library
cap = cv2.VideoCapture("resources\sd.mp4") # read the video
while True: # loop
 success, img = cap.read() # read the video
 cv2.imshow("Video",img) # show the video
 if cv2.waitKey(1) & 0xFF==ord('q'): # press q to quit
    break # break the loop