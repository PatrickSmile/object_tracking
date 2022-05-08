# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np


BLUR = 21
CANNY_THRESH_1 = 18
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 2
MASK_ERODE_ITER = 2
MASK_COLOR = (0,0,0) # In BGR format
 
img = cv2.imread('imposter.jpeg')
cv2.imshow('original', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)
cv2.imshow('edges', edges)

contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
 
mask = np.zeros(edges.shape)

for c in contours:
    cv2.fillConvexPoly(mask, c, (255))

mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)

cv2.imshow('mask', mask)

mask_stack = np.dstack([mask]*3)
mask_stack  = mask_stack.astype('float32') / 255.0
img         = img.astype('float32') / 255.0

masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR)
masked = (masked * 255).astype('uint8')
 
dst = cv2.resize(masked, dsize=(640, 480), interpolation=cv2.INTER_AREA)

cv2.imshow('dst', masked)
cv2.waitKey()
cv2.destroyAllWindows()