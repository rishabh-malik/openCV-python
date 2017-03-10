#simplifying the images in the form of 0 and 1
#made the image bright and readable
import cv2
import numpy as np


img=cv2.imread('bookpage.jpg')
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)         #applying threshold to image, value  above 12 is white and below that is black
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                      #making it gray and then thresholding
retval, threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)



cv2.imshow('original',img)
cv2.imshow('threshold image',threshold)
cv2.imshow('threshold image',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()