import numpy as np
import cv2 as cv

width = 640
height = 640
bpp = 3

# 컬러 이미지를 저장할 Mat 개체를 생성합니다.
img = np.zeros((height, width, bpp), np.uint8)

red = (0,0,255)
green = (0,255,0)
yellow = (0,255,255)

thickness = 2

# polylines를 사용하면 내부가 채워지지 않은 폴리곤을 그립니다.
# polylines의 세번째 아규먼트를 False로 하면
# 시작점과 끝점이 이어지지 않습니다.
pts = np.array([[315,50], [570,240], [475,550], [150,550], [50,240]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, green, thickness)

#fillPoly를 사용하면 내부가 노란색으로 채워진 폴리곤을 그립니다.
pts = np.array([[320,245], [410,315], [380,415], [265,415], [240,315]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], yellow)

cv.imshow("drawing", img)
cv.waitKey(0)