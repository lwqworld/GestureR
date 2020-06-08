"""
get gesture picture data

"""
import os
import cv2 as cv
import numpy as np

capture =cv.VideoCapture(0)
while True:
    ret,frame=capture.read()
    cv.imshow("frame",frame)
    c=cv.waitKey(1)
    if c==ord('q'):
        break
capture.release()
cv.destroyAllWindows()

