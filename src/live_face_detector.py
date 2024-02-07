#!/Users/connorunderwood/anaconda3/bin/python3

import os
import time

import cv2 as cv
import numpy as np


face_cascade = cv.CascadeClassifier('../haar_cascades/haar_frontal_face_default.xml')
eye_cascade = cv.CascadeClassifier('../haar_cascades/haar_frontal_eye.xml')


video = cv.VideoCapture(1)

if not video:
  print("webcam cannot be accessed")

while video.isOpened():
  
  isFrame, frame = video.read()

  if not isFrame:
    print("frame not read")


  gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  
  faces = face_cascade.detectMultiScale(frame, scaleFactor=5, minNeighbors=3)


  for (x,y,w,h) in faces:
    face_boundary =cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
    gray_eyes = gray_scale[y:y+h, x:x+w]
    color_eyes = face_boundary[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(color_eyes, cv.COLOR_BGR2GRAY)
    for (xs, ys, ws, hs) in eyes:
      cv.rectangle(color_eyes, (xs,ys), (xs+ws, ys+hs), (0,255,0), 2)
    
  cv.imshow("Face Detector", frame)


  if cv.waitKey(35) & 0xFF==ord('d'):
    break;

video.release()
cv.destroyAllWindows()




