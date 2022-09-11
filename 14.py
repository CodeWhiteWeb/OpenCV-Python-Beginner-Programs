#Read Webcam
import cv2
# cap = cv2.VideoCapture(0) # 0 for webcam and 1 for external camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # use this for windows 7
cap.set(3,640) # set Width
cap.set(4,480) # set Height
cap.set(10,100)# set Brightness
while True:
 success, img = cap.read() # read the camera
 cv2.imshow("Video",img) # show the camera
 if cv2.waitKey(1) & 0xFF==ord('q'): # press q to quit
    break # break the loop
