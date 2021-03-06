import cv2 as cv
import numpy as np
from random import randint

# 컬러 이미지를 위한 빈 넘파이 배열을 생성합니다.
width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]

for y in range(img_h):
    for x in range(img_w):
        # 픽셀별로 다른 색을 갖도록 0~255 사이의 값을 생성합니다.
        img.itemset(y, x, 0, randint(0, 255)) #b
        img.itemset(y, x, 1, randint(0, 255)) #g
        img.itemset(y, x, 2, randint(0, 255)) #r

cv.imshow("drawing", img)

cv.waitKey(0)