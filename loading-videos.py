import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow('Webcam',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):     #if we press q then the infinite loop breaks
        break

cap.release()
cv2.destroyAllWindows()        