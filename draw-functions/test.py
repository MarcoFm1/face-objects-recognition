import cv2 as cv
import numpy as np

font = cv.FONT_ITALIC
img = np.zeros((512,512,3), np.uint8)
cv.circle(img,(166,345), 63, (247, 168, 239), -1)
cv.circle(img,(300,345), 63, (247, 168, 239), -1)

cv.ellipse(img,(238,200),(80,160),0,180,-180,(247, 168, 239),-1)

cv.putText(img,'test', (170,470), font, 2, (255,255,255), 5, cv.LINE_AA)




while True:
    cv.imshow('test', img)
    
    if cv.waitKey(1) == ord('q'):
        break
