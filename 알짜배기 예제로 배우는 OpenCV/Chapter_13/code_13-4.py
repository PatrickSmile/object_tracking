import cv2 as cv
import numpy as np

# 그레이 스케일로 이미지를 불러옵니다.
src = cv.imread('cat on laptop.jpg', cv.IMREAD_GRAYSCALE)

# 픽셀값의 범위는 0~255이므로 전체 개수는 256개입니다.
histSize = 256

# 픽셀값의 범위는 0~255입니다. 상위경계인 256은 포함되지 않습니다.
histRange = (0,256)

# 히스토그램 막대 크기가 똑같고 처음 시작 시 히스토그램이 비어있도록 합니다.
accumulate = False

# 히스토그램을 계산합니다.
gray_hist = cv.calcHist([src], [0], None, [histSize], histRange, accumulate=accumulate)

# 히스토그램을 보여줄 이미지를 생성합니다.
hist_w = 256
hist_h = 400
histImage = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

# 히스토그램을 정규화합니다.
cv.normalize(gray_hist, gray_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

# 히스토그램을 그려줍니다.
for i in range(0, histSize):

    cv.line(histImage, (i, hist_h - int(np.round(gray_hist[i]))), (i, hist_h - 0), (255,255,255), thickness=2)

# 결과를 화면에 보여줍니다.
cv.imshow('Source image', src)
cv.imshow('Histogram', histImage)
cv.waitKey()