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
img_color