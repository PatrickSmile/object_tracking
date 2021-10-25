import numpy as np
import cv2

# 마우스 클릭한 좌표를 저장할 리스트입니다.
src = np.zeros([4,2], dtype = np.float32)
idx = 0

def mouse_callback(event, x, y, flags, param):
    global point_list, idx

    # 마우스 왼쪽 버튼을 누를 때마다 좌표를 리스트에 저장합니다.
    if event == cv2.EVENT_LBUTTONDOWN:

        src[idx] = (x,y)
        idx = idx + 1

        print("(%d, %d)" %(x,y))

        cv2.circle(img_color, (x,y), 10, (0,0,255), -1)

# 마우스 콜백 함수를 등록합니다.
cv2.namedWindow('original')
cv2.setMouseCallback('original', mouse_callback)

# 사용할 이미지를 불러옵니다.
img_color = cv2.imread('test.jpg')
img_original = img_color

# 반복하면서 마우스 클릭으로 네점을 지정하도록 합니다.
while(True):

    cv2.imshow("original", img_color)

    height, width = img_color.shape[:2]

    # spacebar를 누르면 루프에서 빠져나옵니다.
    if cv2.waitKey(1) == 32:
        break

# 퍼스펙티브 변환 후 영역으로 사각 영역을 지정합니다.
dst = np.float32([[0,0], [width,0], [0,height], [width,height]])

# 퍼스펙티브 변환 행렬을 생성합니다.
M = cv2.getPerspectiveTransform(src, dst)

# 이미지에 퍼스펙티브 변환을 적용합니다.
img_result = cv2.warpPerspective(img_original, M, (width,height))

# 결과를 보여줍니다.
cv2.imshow("result1", img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()