#gradient and edges
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)     #to capture the video through webcam

while True:
    ret, frame=cap.read()

    laplacian=cv2.Laplacian(frame,cv2.CV_64F)                  #gradient
    
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)             #horizontal gradient
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)             #vertical gradient

    edges=cv2.Canny(frame,100,200)                             #to see the edges 

    cv2.imshow('orignal',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        #escape to quit
        break

cap.release()
cv2.destroyAllWindows()          
