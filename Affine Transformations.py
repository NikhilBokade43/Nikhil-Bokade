
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import cv2
import sys


# In[24]:


img = cv2.imread('grid.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)


# - To perform affine oeration we need 3 points on the image 

# In[42]:


#thickness -1 will fill the whole cirlcle
img = cv2.imread('grid.jpg')
rows, cols , chs = img.shape

cv2.circle(img, (84, 90), 5, (255, 0, 0), -1)
cv2.circle(img, (447, 90), 5, (255, 0, 0), -1)
cv2.circle(img, (84, 472), 5, (255, 0, 0), -1)

# pt1 1 is the original points , pt2 is the chnage points position from original
pts1 = np.float32([ [84, 90], [447, 90], [84, 472] ])
pts2 = np.float32([ [84, 154], [447, 140], [100, 472] ])

#create a matrix
matrix = cv2.getAffineTransform(pts1, pts2)
#now tranfor the image using the matrix 
result = cv2.warpAffine(img, matrix ,(rows, cols))

cv2.imshow('x', img)
cv2.imshow('affine tranform', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ![Screenshot%20%284418%29.png](attachment:Screenshot%20%284418%29.png)
