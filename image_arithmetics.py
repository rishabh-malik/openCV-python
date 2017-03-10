import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('pic1.jpg')         #image 2 and 3 are identical in size
img3=cv2.imread('pic2.png')

add=img2+img3                      #to add 2 images one over the another


cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()