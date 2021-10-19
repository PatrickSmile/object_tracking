import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int(width/2), int(height/2))

# center를 중심으로 하는 3개의 원을 그립니다.
# X축 방향 반지름 길이 200, Y축 방향 반지름 길이 10인
# 노란색 타원을 그립니다.
cv.ellipse(img, center, (200,10), 0, 0, 360, (0,255,255), 3)

# X축 방향 반지름 길이10, Y축 방향 반지름 길이 200인
# 녹색 타원을 그립니다.
cv.ellipse(img, center, (10,200), 0, 0, 360, (0, 255, 0), 3)

# X축 방향 반지름 길이 200, y축 방향 반지름 길이 200인
# 빨간색 타원을 그립니다.
cv.ellipse(img, center, (200,200), 0, 0, 360, (0,0,255), 3)

cv.imshow("result", img)
cv.waitKey(0)