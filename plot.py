# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:09:21 2016

@author: Curry
"""



import matplotlib.pyplot as plt
import numpy as np

a=2
b=1
xArray = np.arange( 0, 6, 1.0 )
yArray = a*xArray+b
plt.subplot(211)
plt.plot(xArray,yArray)
plt.plot(xArray,yArray, 'ro')
plt.show()

aArray = np.arange( 0, 6, 1.0 )
plt.subplot(212)
for x in xArray:
    y = a*x+b
    bArray = y-aArray*x
    plt.plot(aArray,bArray)
plt.show()
    