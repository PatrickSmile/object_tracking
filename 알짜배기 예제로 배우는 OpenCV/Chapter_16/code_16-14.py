import cv2 as cv
import numpy as np

img_color = cv.imread('hand.png', cv.IMREAD_COLOR)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# 이미지에 따라 THRESH_BINARY와 THRESH_BINARY_INV를 적절히
# 사용하여 컨투어 검출하려는 객체가 흰색 영역이 되도록 해야합니다.
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_color, contours, 0, (255,0,0), 3)

for contour in contours:
    # 컨투어를 구성하는 모든점을 포함하는 Convex Hull을 구합니다.
    hull = cv.convexHull(contour)

    # Convex Hull을 그려줍니다.
    cv.drawContours(img_color, [hull], 0, (255,0,255), 7)

for contour in contours:
    # 컨투어를 구성하는 모든 점을 포함하는 Convex Hull을 구합니다
    hull = cv.convexHull(contour, returnPoints = False)

    # Convexity Defects를 구합니다.
    defects = cv.convexityDefects(contour, hull)

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        # start와 end를 잇는 직선과 점 far의 거리가 10000 이상
        # 차이나는 경우에만 화면에 그려줍니다.
        # far가 Convexity Defects 위치입니다.
        if d > 10000:
            cv.line(img_color, start, end, (0,255,0), 3)
            cv.circle(img_color, far, 5, (0,0,255), -1)

cv.imshow("result", img_color)
cv.waitKey(0)