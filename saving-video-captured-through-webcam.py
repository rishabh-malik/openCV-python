import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)     #to capture the video through webcam
fourcc=cv2.VideoWriter_fourcc(*'XDIV')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame=cap.read()
    out.write(frame)
    cv2.imshow('Webcam',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):     #if we press q then the infinite loop breaks
        break

cap.release()
out.release()
cv2.destroyAllWindows()        