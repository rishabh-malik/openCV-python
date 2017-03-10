import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('pic1.jpg')         #image 2 and 3 are identical in size
img3=cv2.imread('pic2.png')

#add=img2+img3                      #to add 2 images one over the another
#add=cv2.add(img2,img3)              #adding the pixel color value of the 2 pictures
weighted=cv2.addWeighted(img2,0.6,img3,0.3,0)     #giving img2 a weight of 0.6 and img3 0.3 weight and then adding them

#cv2.imshow('add',add)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()