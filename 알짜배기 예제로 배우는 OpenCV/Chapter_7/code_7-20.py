import numpy as np
import cv2 as cv

img_w = 640
img_h = 480
bpp = 3

# 컬러 이미지를 저장할 Mat 개체를 생성합니다.
img = np.zeros((img_h, img_w, bpp), np.uint8)

red = (0,0,255)
green = (0,255,0)
white = (255,255,255)
yellow = (0,255,255)

# 이미지 중앙을 기준으로 문자열을 배치하기 위해 사용합니다.
center_x = int(img_w/2.0)
center_y = int(img_h/2.0)

# 4가지 폰트를 사용하여 글자를 출력해봅니다.
thickness = 2

location = (center_x - 200, center_y - 100)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 3.5
cv.putText(img, 'OpenCV', location, font, fontScale, yellow, thickness)

location = (center_x - 150, center_y + 20)
font = cv.FONT_ITALIC
fontScale = 2
cv.putText(img, 'Tutorial', location, font, fontScale, red, thickness)

location = (center_x - 250, center_y + 100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
cv.putText(img, 'webnautes.tistory.com', location, font, fontScale, white, thickness)

location = (center_x - 130, center_y +150)
font = cv.FONT_HERSHEY_COMPLEX # normal size serif font
fontScale = 1.2
cv.putText(img, 'webnautes', location, font, fontScale, green, thickness)

cv.imshow("drawing", img)
cv.waitKey(0)