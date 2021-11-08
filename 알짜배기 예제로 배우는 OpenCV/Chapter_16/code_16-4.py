import cv2 as cv

img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# 이미지에 따라 THRESH_BINARY와 THRESH_BINARY_INV를 적절히
# 사용하여 컨투어 검출하려는 객체가 흰색 영역이 되도록 해야합니다.
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_color, contours, 0, (0,0,255), 3)
cv.drawContours(img_color, contours, 1, (0,255,0), 3)

# 컨투어 영역의 크기를 계산하여 출력합니다.
for i, contour in enumerate(contours):
    area = cv.contourArea(contour)

    print(i, '-', area)

cv.imshow("result", img_color)
cv.waitKey(0)