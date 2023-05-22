#Import librery and modules
import numpy as np
import cv2 as cv

#Capture video from laptop camera
cap = cv.VideoCapture(0) #Zero means that you will use the device default camera

#If camera is not open, end the script and close
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame and return two variables
    ret, frame = cap.read() #ret reads if the frame was correctly read or no (boolean), if it's true lo almacena en la variable frame

    if not ret:
        print("Exiting ...")
        break
    
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('window-name', gray)
    if cv.waitKey(1) == ord('q'):   
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()