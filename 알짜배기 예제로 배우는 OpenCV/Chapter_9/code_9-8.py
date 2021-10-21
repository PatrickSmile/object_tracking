import numpy as np
import cv2 as cv

point_list = []

def mouse_callback(event, x, y, flags, param):

    # 마우스 왼쪽 버튼을 누를 때마다 좌표를 리스트에 저장합니다.
    if event == cv.EVENT_LBUTTONDOWN:

        print("(%d, %d)" %(x,y))

        point_list.append((x,y))
        cv.circle(img_color, (x,y), 3, (0,0,255), -1)

# 마우스 콜백함수를 등록합니다.
cv.namedWindow('source')
cv.setMouseCallback('source', mouse_callback)

# 사용할 이미지를 불러옵니다.
img_color = cv.imread('test.png')

# 반복하면서 마우스 클릭으로 세 점을 지정하도록 합니다.
while(True):

    cv.imshow('source', img_color)

    # spacebar를 누르면 루프에서 빠져나옵니다.
    if cv.waitKey(1) == 32:
        break

height, weight = img_color.shape[:2]

# 오른쪽 상단의 대응점만 Y좌표가 아래로 100 이동하도록 지정합니다.

pts1 = np.float32([point_list[0], point_list[1], point_list[2]])
pts2 = np.float32([point_list[0], point_list[1], point_list[2]])
pts2[1][1] += 100

# 아핀 변환 행렬을 생성합니다.
M = cv.getAffineTransform(pts1, pts2)

# 이미지에 아핀 변환 행렬을 적용합니다.
img_result = cv.warpAffine(img_color, M, (weight, height))

# 결과를 보여줍니다.
cv.imshow("result", img_result)
cv.waitKey(0)
cv.destroyAllWindows()
