import numpy as np
import cv2 as cv

# 컬러 이미지를 위한 빈 넘파이 배열을 생성합니다.
width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

# 이미지의 너비, 높이, 채널 수 를 가져오는 방법입니다.
img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)

# 그리기 함수에서는 좌표를 (x,y) 순으로 적습니다.
# (x,y) = (100, 300)위치에 노란색 원을 그립니다.
# 나머지 아규먼트는 뒤에서 다룹니다.
cv.circle(img, (100, 300), 10, (0, 255, 255), -1)

cv.imshow("drawing", img)

cv.waitKey(0);