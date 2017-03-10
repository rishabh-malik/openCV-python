#getting rid of background to extract foreground
#used only for extracting action from videos
#currently working only for webcam not for video loaded 
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture('people-walking.mp4')
fgbg=cv2.createBackgroundSubtractorMOG2()       #for creating background

while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)                    #apply mask to video

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()        