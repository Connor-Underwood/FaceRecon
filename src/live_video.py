#!/Users/connorunderwood/anaconda3/bin/python3

import numpy as np
import cv2 as cv


def rescaleFrame(frame, scale=.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def rotateFrame(img, angle, rotPoint=None):
  
  (width,height) = img.shape[:2]

  if not rotPoint:
    rotPoint = (width//2, height//2)

  rotationMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width,height)
  return cv.warpAffine(img, rotationMatrix, dimensions)
  	




  


# Returns a VideoCapture Object
video = cv.VideoCapture(1)


if video == None:
    print("video not found")

while video.isOpened():
    # read() returns 1) a boolean if the frame was read or not and 2) the actual frame object
    try:
        readFrame, frame = video.read()
    except:
        print("frame not found")

    if not readFrame:
        print("frame not read")

    # resizing a frame
    frame_resized = rescaleFrame(frame)

    # grayscaling a frame
    gray_scale =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # blurring a frame
    blur = cv.GaussianBlur(frame, (1,1), cv.BORDER_DEFAULT)

    # edge cascading
    canny = cv.Canny(frame, 125, 175)

    # rotating a frame
    rotated = rotateFrame(frame, -180)

    # thresholding a frame
    ret, thresh = cv.threshold(gray_scale,125, 255, cv.THRESH_BINARY)
    cv.imshow('Threshold frame', thresh)
    
    #cv.imshow('Rotated Frames', rotated)

    #cv.imshow("Canny Edge Detection", canny)

    # Show the actual frame on a display called 'Video'
    #cv.imshow('Video', frame)

    #Testing out rescaleFrame
    #cv.imshow('Video Resized', frame_resized)

    #cv.imshow('GrayScale', gray_scale)
    #cv.imshow('Blur', blur)



    if cv.waitKey(35) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
