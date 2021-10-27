import cv2 as cv
import numpy as np

# 이미지를 불러옵니다.
src = cv.imread('apple.jpg', cv.IMREAD_COLOR)

# 컬러 이미지를 B, G, R 채널로 분리합니다.
bgr_planes = cv.split(src)

# 픽셀값의 범위는 0~255이므로 전체 개수는 256개입니다.
histSize = 256

# 픽셀값의 범위는 0~255입니다. 상위 경계인 256은 포함되지 않습니다.
histRange = (0, 256)

# 히스토그램 막대 크기가 똑같고 처음 시작 시 히스토그램이 비어있도록 합니다.
accumulate = False

# B, G, R 채널별로 히스토그램을 계산합니다.
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)

# 히스토그램을 보여줄 이미지를 생성합니다.
hist_w = 256*3
hist_h = 400
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

# 히스토그램을 정규화 합니다.
cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

# 히스토그램을 그려줍니다.
for i in range(0, histSize):

    # 파란색 히스토그램
    cv.line(histImage, (i, hist_h - int(np.round(b_hist[i]))), (i, hist_h - 0), (255,0,0), thickness=2)

    # 녹색 히스토그램
    cv.line(histImage, (i + 256, hist_h - int(np.round(g_hist[i]))), (i + 256, hist_h - 0), (0, 255, 0), thickness=2)

    # 빨간색 히스토그램
    cv.line(histImage, (i + 256*2, hist_h - int(np.round(r_hist[i]))), (i + 256*2, hist_h - 0), (0, 0, 255), thickness=2)

# 결과를 화면에 보여줍니다.
cv.imshow('Source image', src)
cv.imshow('Histogram', histImage)
cv.waitKey()