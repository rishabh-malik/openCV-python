import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)     #to capture the video through webcam

while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #for showing the video in gray mode
    cv2.imshow('Webcam',frame)
    cv2.imshow('Webcam gray',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):     #if we press q then the infinite loop breaks
        break

cap.release()
cv2.destroyAllWindows()        