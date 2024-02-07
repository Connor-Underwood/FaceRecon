#!/Users/connorunderwood/anaconda3/bin/python3

import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('../haar_cascades/harr_frontal_face_default.xml')
eye_cascade = cv.CascadeClassifier('../haar_cascades/haar_frontal_eye.xml')



