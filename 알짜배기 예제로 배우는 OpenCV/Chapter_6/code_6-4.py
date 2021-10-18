import cv2 as cv

# 사람이 없을 때 이미지 background.png와
# 사람이 있을 때 이미지 object.png를 불러옵니다.
img_background = cv.imread('background.png', cv.IMREAD_GRAYSCALE)
img_object = cv.imread('object.png', cv.IMREAD_GRAYSCALE)

# 사람이 있는 이미지 img_object에서
# 사람이 없는 이미지 img_background를 빼서 차영상을 얻습니다.