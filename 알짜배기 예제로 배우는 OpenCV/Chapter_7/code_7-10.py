import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

# 화면 중앙을 가로질러 선굵기 3인 대각선을 2개 그려 교차하도록 합니다.
cv.line(img, (width-1, 0), (0, height-1), (0, 255, 0), 3)
cv.line(img, (0,0), (width-1, height-1), (0, 0, 255), 3)

cv.imshow("result", img)
cv.waitKey(0)
