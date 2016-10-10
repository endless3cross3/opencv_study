# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 08:09:43 2016

@author: Curry
"""

import numpy as np
import cv2

filePath = 'map.png'
img = cv2.imread(filePath)   
height, width = img.shape[:2] # get height, width

row = 0
while row < height:
    row = row + 65
    cv2.line(img,(0,row),(width,row),(0,255,0),1)
    
column = 43
while column < width:
    column = column + 65
    cv2.line(img,(column,0),(column,height),(0,255,0),1)    

cv2.imwrite('new_50m_map.png',img)
print("OK!")

cv2.namedWindow("Image")   
cv2.imshow("Image", img)   
key = cv2.waitKey (0) 
cv2.destroyAllWindows()