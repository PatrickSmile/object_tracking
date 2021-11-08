import cv2 as cv

# 컬러로 이미지를 가져옵니다.
img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)

# 그레이 스케일로 변환한 후, 이진화하여 바이너리 이미지로 변환합니다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)

# 이진화 결과를 개선하기 위해 모폴로지 연산을 해줍니다.
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

# 컨투어를 검출합니다.
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 검출된 2개의 컨투어를 이미지에 그려줍니다.
# 각각 인덱스 0, 인덱스 1로 지정할 수 있습니다.
cv.drawContours(img_color, contours, 0, (0,0,255), 3)
cv.drawContours(img_color, contours, 1, (0,255,0), 3)

# 다음처럼 한번에 모든 컨투어를 그릴 수도 있습니다.
# cv.drawContours(img_color, contours, -1, (0,,255,0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)