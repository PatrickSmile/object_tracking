import cv2 as cv
import numpy as np

# 이미지를 불러옵니다.
img_color = cv.imread('cat.jpg')
cv.imshow("original", img_color)

height, width = img_color.shape[:2]

# 이미지를 오른쪽으로 100, 아래로 50 이동시키는 이동 행렬을 만듭니다.
M = np.float32([[1, 0, 100], [0, 1, 50]])

# 이동 행렬을 이미지에 적용합니다.
img_translation = cv.warpAffine(img_color, M, (width, height))

cv.imshow("translation", img_translation)

cv.waitKey(0)
cv.destroyAllWindows()