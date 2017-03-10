#used to show or delete a specific color from a picture or a video
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)     #to capture the video through webcam

while True:
    ret, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                        #hue saturation value

    lower_blue=np.array([100,100,0])
    upper_blue=np.array([255,255,255])

    mask=cv2.inRange(hsv,lower_blue,upper_blue)                      #mask contains everything that contains within the ranges
    res=cv2.bitwise_and(frame,frame,mask=mask)     
    
    cv2.imshow('frame',frame)                  
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        #escape to quit
        break

cap.release()
cv2.destroyAllWindows()          
