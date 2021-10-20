import cv2 as cv

# 이미지를 불러옵니다.
img_color = cv.imread('cat.jpg')
cv.imshow("original", img_color)

# fx, fy를 사용하여 이미지 확대 및 축소 비율을 적어줄 수 있습니다.
# 여기에선 가로 방향(fx)으로 2개, 세로 방향(fy)으로 3배 확대합니다.
# 이미지 확대 시에는 보간법으로 INTER_CUBIC을 권장합니다.
img_result = cv.resize(img_color, )