import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

px=img[55,55]
print(px)                  #to print the color value of that co ordinate

img[55,55]=[255,255,0]     #changing the color of that coordinate
print(px)

img[100:150,100:150]=[255,255,255]       #changing that image portion to white-ROI(region of image)

face=img[40:100,50:100]                  #copy and pasting regions of space
img[0:60,0:50]=face

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()