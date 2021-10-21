import cv2 as cv

# 이미지를 불러옵니다.
img_color = cv.imread('cat.jpg')
cv.imshow("original", img_color)

# fx, fy를 사용하여 이미지 확대 및 축소 비율을 적어줄 수 있습니다.
# 여기에선 가로 방향(fx)으로 2개, 세로 방향(fy)으로 3배 확대합니다.
# 이미지 확대 시에는 보간법으로 INTER_CUBIC을 권장합니다.
img_result = cv.resize(img_color, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow("x2 INTER_CUBIC", img_result)

# 확대 및 축소되는 이미지 크기를 너비와 높이로 지정할 수 있습니다.
# 여기에서는 너비와 높이를 3배 확대합니다.
height, width = img_color.shape[:2]
img_result = cv.resize(img_color, (3*width, 3*height), interpolation = cv.INTER_LINEAR)
cv.imshow("x3 INTER_LINEAR", img_result)

# 이미지의 너비와 높이를 0.5배 줄입니다.
img_result = cv.resize(img_color, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
cv.imshow("x0.5 INTER_AREA", img_result)

cv.waitKey(0)
cv.destroyAllWindows()