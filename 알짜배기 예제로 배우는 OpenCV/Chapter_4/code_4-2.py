import cv2 as cv

# 트랙바를 조정할 때마다 실행되는 콜백함수입니다.
# 이곳에 트랙바로 조정할 OpenCV함수를 넣을 수 있습니다.
# 여기에서는 아무 일하지 않는 더미함수로 정의합니다.
def on_trackbar(x):
    pass

# namedWindow함수를 사용하여 트랙바를 붙일 윈도우를 생성해야 합니다.
cv.namedWindow('Canny')

# 트랙바를 생성합니다.
# 트랙바 이름, 윈도우 이름, 트랙바의 최솟값, 최댓값, 콜백함수를 입력합니다.
cv.createTrackbar('low threshold', 'Canny', 0, 1000, on_trackbar)
cv.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)

# 트랙바의 초기값을 설정해줍니다.
# 트랙바 이름, 트랙바가 붙어있는 윈도우 이름으로 트랙바에 접근합니다.
cv.setTrackbarPos('low threshold', 'Canny', 50)
cv.setTrackbarPos('high threshold', 'Canny', 150)

# 이미