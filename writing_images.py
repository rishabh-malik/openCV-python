import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

font=cv2.FONT_ITALIC
cv2.putText(img,'hey! its me',(100,130),font,1,(255,255,0),2,cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()