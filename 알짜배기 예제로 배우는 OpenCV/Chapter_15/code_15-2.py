import cv2 as cv

# 이미지 파일을 불러와 그레이 이미지로 변환합니다.
img_gray = cv.imread("gradation.png", cv.IMREAD_GRAYSCALE)

# 임계값을 127로 해서 이진화 합니다.
# 입력 이미지의 특정 픽셀값이 임계값보다 크면 결과
# 이미지상의 같은 위치의 픽셀값을 255로 입력합니다.
# 임계값보다 작을 경우에는 0이 됩니다.
ret, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

cv.imshow("grayscale", img_gray)
cv.imshow("binary", img_binary)

cv.waitKey(0)