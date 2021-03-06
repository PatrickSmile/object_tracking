import cv2 as cv

# 사람이 없을 때 이미지 background.png와
# 사람이 있을 때 이미지 object.png를 불러옵니다.
img_background = cv.imread('background.png', cv.IMREAD_GRAYSCALE)
img_object = cv.imread('object.png', cv.IMREAD_GRAYSCALE)

# 사람이 있는 이미지 img_object에서
# 사람이 없는 이미지 img_background를 빼서 차영상을 얻습니다.
# 빼는 순서를 바꾸면 안됩니다.
img_sub = cv.subtract(img_object, img_background)

# 차영상을 이진화합니다.
retval, img_binary = cv.threshold(img_sub, 50, 255, cv.THRESH_BINARY)

cv.imshow('background', img_background)
cv.imshow('object', img_object)
cv.imshow('sub', img_sub)
cv.imshow('binary', img_binary)
cv.waitKey(0)