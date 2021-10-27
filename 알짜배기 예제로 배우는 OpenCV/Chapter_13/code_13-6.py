import cv2 as cv
import numpy as np

def draw_histgram(img):

    # 히스토그램을 그릴 이미지를 생성합니다.
    hist_h = img.shape[0]
    hist_w = 256
    img_histogram1 = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

    # 히스토그램을 계산하여 그립니다.
    histSize = 256
    histRange = (0,256)
    accumulate = False
    hist_item = cv.calcHist([img], [0], None, [histSize], histRange, accumulate=accumulate)

    cv.normalize(hist_item, hist_item, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

    for i in range(0, histSize):

        cv.line(img_histogram1, (i, hist_h - int(np.round(hist_item[i]))), (i, hist_h - 0), (255,255,255))

    # 누적 히스토그램을 그릴 이미지를 생성합니다.
    img_histogram2 = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

    # 누적 히스토그램을 계산하여 그립니다.
    c_hist = np.zeros(hist_item.shape, dtype=hist_item.dtype)

    c_hist[0] = hist_item[0]
    for i in range(1, hist_item.shape[0]):
        c_hist[i] = hist_item[i] + c_hist[i-1]

    cv.normalize(c_hist, c_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

    for i in range(1, histSize):
        pts = []
        pts.append((i, hist_h - np.round(c_hist[i])))
        pts.append(((i-1), hist_h - np.round(c_hist[i-1])))
        pts = np.array(pts, dtype=np.int32)
        pts = np.int32(pts)
        cv.polylines(img_histogram2, [pts], False, (255,255,255))

    result = cv.hconcat((img_histogram1, img_histogram2))

    return result

# 이미지를 그레이 스케일로 불러옵니다.
img_gray = cv.imread('test1.png', cv.IMREAD_GRAYSCALE)

# 원본 이미지에 대한 히스토그램을 그립니다.
img_histo1 = draw_histgram(img_gray)

result1 = cv.hconcat((img_gray, img_histo1))

cv.imshow('result1', result1)

# 히스토그램 평활화를 적용 후, 히스토그램을 그립니다.
img_equ = cv.equalizeHist(img_gray)
img_histo2 = draw_histgram(img_equ)
result2 = cv.hconcat((img_equ, img_histo2))
cv.imshow('result2', result2)

cv.waitKey(0)
cv.destroyAllWindows()
