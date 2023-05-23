import cv2 as cv

cam = cv.VideoCapture(0)

if not cam.isOpened():
    print('bye')
    exit()

while True:
    ret, frame = cam.read()

    if ret == False:
        print('bye')
        exit()

    flipped_frame = cv.flip(frame, 1)  # flip frames (video) -X

    cv.imshow('window-name', flipped_frame)

    if cv.waitKey(1) == ord('q'):   
        break

cam.release()
cv.destroyAllWindows()