import cv2 as cv

img_color = cv.imread('square.png', cv.IMREAD_COLOR)

# 이미지에 따라 THRESH_BINARY와 THRESH_BINARY_INV를 적절히
# 사용하여 컨투어 검출하려는 객체가 흰색 영역이 되도록 해야 합니다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_color, contours, 0, (0,0,255), 3)

for contour in contours:

    # 컨투어를 직선으로 근사화합니다.
    epsilon = 0.03 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    # 근사화한 직선을 이미지에 그려줍니다.
    cv.drawContours(img_color, [approx], 0, (0,255,0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)