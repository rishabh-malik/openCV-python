import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('pic1.jpg')     

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV) #will convert the white areas to black and vica versa


cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()