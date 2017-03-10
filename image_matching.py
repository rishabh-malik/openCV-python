#finding image in some image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bgr=cv2.imread('pic.jpg')
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

template=cv2.imread('template.jpg',0)               #template to find
w,h=template.shape[::-1]                            #to get width and height of template

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.9                                        #the template should match the content of image 90%

loc=np.where(res>=threshold)

for pt in zip(*loc[::-1]):                                             #to draw a rectangle on the detected image
    cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255))

cv2.imshow('detected',img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
