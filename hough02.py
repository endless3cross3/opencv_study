# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 00:53:08 2016

@author: Curry
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import cv2  
import numpy as np 

img = cv2.imread("road.jpg")  
  
img = cv2.GaussianBlur(img,(3,3),0)  
edges = cv2.Canny(img, 50, 150, apertureSize = 3)  
lines = cv2.HoughLines(edges,1,np.pi/180,118)  
result = img.copy()  
  
#经验参数  
minLineLength = 200  
maxLineGap = 15  
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)  
for x1,y1,x2,y2 in lines[0]:  
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)  
  
cv2.imshow('Result', img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  