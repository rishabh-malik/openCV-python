import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,0,0),15)                      #to draw a line #255,0,0 for blue - BGR
cv2.rectangle(img,(50,50),(100,100),(255,255,255),2)            #to draw a rectangle
cv2.circle(img,(500,500),55,(0,0,255),-1)                       #to draw a circle #-1 to fill in the circle

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)         #points of the polygon
cv2.polylines(img,[pts],True,(0,255,255),3)                     #to draw on the polygon

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()