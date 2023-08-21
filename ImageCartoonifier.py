# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:17:53 2023

@author: Shimon
"""
#for image processing
#pip install opencv-python
import cv2

#pip install numpy
import numpy as np

#Reading the image
myimg=cv2.imread("man.JPG")

graying=cv2.cvtColor(myimg,cv2.COLOR_BGRA2GRAY)

graying=cv2.medianBlur(graying,9)

edges=cv2.adaptiveThreshold(graying,300,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

color=cv2.bilateralFilter(myimg,255,100,400)

cartoon=cv2.bitwise_and(color,color,mask=edges)

#Final Cartoon Image
cv2.imwrite("result.png",cartoon)


cv2.waitKey(0)

cv2.destroyAllWindows();