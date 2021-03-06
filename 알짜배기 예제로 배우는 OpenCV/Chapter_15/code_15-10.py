import cv2 as cv
import numpy as np
import os

# 웹캠 영상을 테스트하려면 아규먼트를 0으로 수정하세요.
cap = cv.VideoCapture(0)

# 환경에 따라 두 번째 아규먼트를 조정하세요.
foregroundBackground = cv.createBackgroundSubtractorMOG2(history = 500, varThreshold=250, detectShadows=False)

while(1):
    ret, img_frame = cap.read()
    if ret == False:
        break

    blur = cv.GaussianBlur(img_frame, (5,5), 0)

    # 배경을 제거하고 오브젝트 영역만 보이는 마스크 이미지를 만듭니다.
    img_mask = foregroundBackground.apply(blur, learningRate=0)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)

    cv.imshow('mask', img_mask)
    cv.imshow('color', img_frame)

    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()