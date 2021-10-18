import cv2 as cv
import sys

# 트랙바를 위한 콜백함수입니다.
def on_trackbar(x):
    pass

# 이미지를 읽어옵니다.
img_color = cv.imread("red ball.png", cv.IMREAD_COLOR)
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)

# 그레이 스케일 이미지로 변환합니다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', img_gray)

# 윈도우에 트랙바를 추가합니다.
cv.namedWindow("Binary")
cv.createTrackbar("threshold", "Binary", 0, 255, on_trackbar)
cv.setTrackbarPos("threshold", "Binzary", 127)

# 트랙바를 사용하여 파라미터를 조정할 OpenCV함수를 콜백함수에 넣는
# 대신 필요한 부분에 루프를 추가하여 처리합니다.
while True:

    # 트랙바의 값을 읽어와 threshold함수를 위한 파라미터로 사용합니다.
    thresh = cv.getTrackbarPos("threshold", "Binary")

    # 빨간색 공 영역의 픽셀값이 배경보다 작기 때문에
    # THRESH_BINARY_INV를 사용하여 임계값보다 작은 영역이
    # 흰색 영역이 되도록 합니다.
    retval, img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY_INV)

    # 결과 이미지를 보여줍니다.
    cv.imshow("Binary", img_binary)

    # ESC키를 누를때 루프에서 빠져나오도록 합니다.
    if cv.waitKey(1) & 0xFF == 27:
        break