#Import modules and library
import cv2 as cv
import sys

#Take an image
img = cv.imread("emma_myers.png")

#If image is empty, close the program
if img is None:
    sys.exit('No image')

#Show image previously taken 
cv.imshow('Showing image',img)

quit = cv.waitKey(0)

if quit == ord('q'):
    cv.imwrite("emma_myers.png", img)