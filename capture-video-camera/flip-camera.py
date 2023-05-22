import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('test.avi', fourcc, 30.0, (1920,  1080))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("camera cannot start")
        break
    frame = cv.flip(frame, 0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    # write the flipped frame
    out.write(gray)
    cv.imshow('xd', gray)
    
    if cv.waitKey(1) == ord('q'):
        break
