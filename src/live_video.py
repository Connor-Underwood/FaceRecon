#!/home/underw23/anaconda3/bin/python3

import numpy as np
import cv2 as cv


def rescaleFrame(frame, scale=.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# Returns a VideoCapture Object
video = cv.VideoCapture("../videos/connor_smol.mp4")



if video == None:
    print("video not found")

while True:
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

    cv.imshow("Canny Edge Detection", canny)

    # Show the actual frame on a display called 'Video'
    cv.imshow('Video', frame)

    #Testing out rescaleFrame
    #cv.imshow('Video Resized', frame_resized)

    #cv.imshow('GrayScale', gray_scale)
    #cv.imshow('Blur', blur)



    if cv.waitKey(35) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
