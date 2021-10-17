import cv2 as cv
import sys

# 이미지를 읽어옵니다.
img_color = cv.imread('grayscale.png', cv.IMREAD_COLOR)
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)

# 그레이 스케일 이미지로 변환합니다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# 임계값 127을 사용하여 이진화 합니다.
# 이진화 타입으로 THRESH_BINARY를 사용하면
# 픽셀값이 127 보다 크면 255, 127이하이면 0이 됩니다.
# 이진화 타입으로 THRESH_BINARY_INV를 사용하면 반대로 됩니다.
retval, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# 결과 이미지를 보여줍니다.
cv.imshow("Grayscale", img_gray)
cv.imshow("Binary", img_binary)
cv.waitKey(0)

