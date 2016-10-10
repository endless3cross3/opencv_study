# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:57:24 2016

@author: Curry
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import cv2  
import numpy as np  
   
img = cv2.imread("lion.jpg", 0)  
  
img = cv2.GaussianBlur(img,(3,3),0)  
canny = cv2.Canny(img, 50, 150)  
  
cv2.imshow('Canny', canny)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  