#used to remove noise 
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
    

    #erosion-if all pixels in area are identical color then if moves on but if any pixel is not of same color it removes it
    #dilation- instead of eroding away it pushes everything

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=0)

    #opening- removes false positives
    #closing- removes false negative

    opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    
    cv2.imshow('frame',frame)                  
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)                  
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)                  
    cv2.imshow('closing',closing)

    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        #escape to quit
        break

cap.release()
cv2.destroyAllWindows()          
