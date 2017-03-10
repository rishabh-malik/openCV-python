#simplifying the images in the form of 0 and 1
#made the image bright and readable
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('bookpage.jpg')
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)         #applying threshold to image, value  above 12 is white and below that is black

cv2.imshow('original',img)
cv2.imshow('threshold image',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()