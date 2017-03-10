import cv2
import numpy as np
import matplotlib.pyplot as plt

smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml') #loading the smile cascade

cap=cv2.VideoCapture(0)     #to capture the video through webcam

while True:
    ret, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    smile=smile_cascade.detectMultiScale(gray,4.0,6)                    #detecting the smile in gray since it is easy to detect in gray
    for (x,y,w,h) in smile:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow('img',img)
    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        #escape to quit
        break

cap.release()
cv2.destroyAllWindows()  