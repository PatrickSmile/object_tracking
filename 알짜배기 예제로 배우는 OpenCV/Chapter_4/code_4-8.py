import cv2 as cv
import sys

img_color = cv.imread("ball.png", cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)

# 그레이 스케일 이미지로 변환합니다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# Canny를 사용하여 에지를 검출합니다.
img_canny = cv.Canny(img_gray, 90, 180)

# 윈도우별로 처리 결과를 보여줍니다.
cv.imshow("Grayscale", img_gray)
cv.imshow("Canny", img_canny)

cv.waitKey(0)
cv.destroyAllWindows()