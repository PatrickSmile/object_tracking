import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 640
height = 480
bpp = 3
img = np.zeros((height, width, bpp), np.uint8)

center = (int(width/2), int(height/2))

# center를 중심으로 하는 3개의 원을 그립니다.

# X축 방향 반지름 길이 10, Y축 방향 반지름 길이 200인
# 녹색 타원을 그립니다.
# 수직선에 가까운 타원이 그려집니다.
cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3)

# 빨간색 타원을 시계 방향으로 45도 회전하여 그립니다.
cv.ellipse(img, center, (10, 200), 45, 0, 360, (0,0,255), 3)

# 노란색 타원을 반시계 방향으로 45도 회전하여 그립니다.
cv.ellipse(img, center, (10, 200), -45, 0, 360, (0,255,255), 3)

cv.imshow("result", img)
cv.waitKey(0)