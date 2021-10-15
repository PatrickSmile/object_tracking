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

# 연결할 이미지를 hconcat/vconcat의 아규먼트로 입력합니다.
# 같은 타입의 이미지여야 합니다.

# 수평 방향으로 matrices에 포함된 이미지를 연결합니다.
img_result = cv.hconcat([img_gray, img_canny])

# 수직 방향으로 matrices에 포함된 이미지를 연결합니다.
# img_result = cv.vconcat([img_gray, img_canny])

cv.imshow('Result', img_result)
cv.waitKey(0)

cv.destroyAllWindows()