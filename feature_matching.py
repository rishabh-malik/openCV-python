#used for matching images not very accurate
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('feature_template.jpg',1)
img2=cv2.imread('feature-matching-image.jpg',1)

orb=cv2.ORB_create()                                       #orb detector

kp1,des1=orb.detectAndCompute(img1,None)                   #keypoints and descriptors          
kp2,des2=orb.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)         #Bf matcher object

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)

img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)   #shows 10 matches
plt.imshow(img3)
plt.show()


