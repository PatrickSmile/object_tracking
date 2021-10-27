import numpy as np
import cv2 as cv

# 그레이 스케일로 입력 이미지를 불러옵니다.
img_gray = cv.imread('test2.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.medianBlur(img_gray, 5)

# 결과 이미지에 컬러 도형을 사용하기 위해 컬러로 변환합니다.
img_color = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# 원을 검출합니다.
circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=35, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

# 검출된 원에 빨간색/초록색 원을 그려줍니다.
for c in circles[0,:]:

    center = (c[0], c[1])
    radius = c[2]

    # 바깥 원
    cv.circle(img_color, center, radius, (0,255,0), 2)

    # 중심 원
    cv.circle(img_color, center, 2, (0,0,255), 3)

# 검출 결과를 화면에 보여줍니다.
cv.imshow('detected circles', img_color)
cv.waitKey(0)
cv.destroyAllWindows()