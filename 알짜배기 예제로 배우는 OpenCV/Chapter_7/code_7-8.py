import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

# (320,240)이 중심인 반지름 10인 초록색으로 채워진 원을 그립니다.
cv.circle(img, (320, 240), 10, (0, 255, 0), -1)

# (320,240)이 중심인 반지름이 100인 선굵기가 1인 빨간색 원을 그립니다.
cv.circle(img, (320, 240), 100, (0, 0, 255), 1)

cv.imshow("result", img)
cv.waitKey(0)