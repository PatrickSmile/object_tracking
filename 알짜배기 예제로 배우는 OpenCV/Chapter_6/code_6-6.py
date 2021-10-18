import cv2 as cv
import numpy as np

# 사용할 이미지를 불러옵니다.
img_logo = cv.imread('logo.png', cv.IMREAD_COLOR)
img_background = cv.imread('background.png', cv.IMREAD_COLOR)

# 로고를 이진화합니다.
img_gray = cv.cvtColor(img_logo, cv.COLOR_BGR2GRAY)
ret, img_mask = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)

# 배경 지우고 로고만 배경 이미지에 보여주려면 반전된
# 이진화 이미지도 필요합니다.
img_mask_inv = cv.bitwise_not(img_mask)

# 로고 이미지 크기만큼 배경 이미지를 잘라냅니다.
# 로고가 삽입될 위치가 됩니다.
height, width = img_logo.shape[:2]
img_roi = img_background[0:height, 0:width]

# 이진화 이미지를 사용하여 로고 이미지에서는 배경을 지우고
# 배경 이미지에서는 로고가 들어갈 위치를 제거합니다.
img1 = cv.bitwise_and(img_logo, img_logo, mask = img_mask_inv)
img2 = cv.bitwise_and(img_roi, img_roi, mask = img_mask)

# bitwise_and 함수를 사용한 결과를 더하면
# 배경 이미지에 로고가 합성된 결과를 얻을 수 있습니다.
dst = cv.add(img1, img2)

# 합성 결과를 배경 이미지에 복사해줍니다.
img_background[0:height, 0:width] = dst

# 결과를 보여줍니다.
cv.imshow('background', img_background)
cv.imshow('logo', img_logo)
cv.imshow('img_mask_inv', img_mask_inv)
cv.imshow('img_mask', img_mask)
cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('dst', dst)
cv.waitKey(0)
