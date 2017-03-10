#used for motion tracking and character recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('corner_detection.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)        #no of corners, image quality, min distance b/w corners

