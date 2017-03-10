#haar cascades- face and eye detection
#these are xml files with feature sets
#download haarcascades in order to use them
import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface.xml') #loading the face cascade
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml') #loading the eye cascade

cap=cv2.VideoCapture(0)     #to capture the video through webcam

while True:
    ret, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)                    #detecting the face in gray since it is easy to detect in gray
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+h]                                     #a region of space in the face
        roi_color=img[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray)                   #detecting the eyes inside the face
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        #escape to quit
        break

cap.release()
cv2.destroyAllWindows()  