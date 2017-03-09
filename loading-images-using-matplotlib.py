import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot()
plt.show()