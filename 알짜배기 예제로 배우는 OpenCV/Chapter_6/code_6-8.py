import cv2 as cv

img_color = cv.imread('green.png', cv.IMREAD_COLOR)

height, width = img_color.shape[:2]
center_x, center_y = int(width*0.5), int(height*0.5)

# 이미지 중심에서 일정 거리를 ROI 영역으로 합니다.
# copy 메소드를 사용하면 원본 이미지 수정 없이 ROI 영역을 다룰 수 있습니다.
img_roi = img_color[center_y-100:center_y+100, center_x-100:center_x+100].copy()

# ROI 영역을 그레이 스케일로 변환한 후, 케니 에지를 구합니다.
img_gray = cv.cvtColor(img_roi, cv.COLOR_BGR2GRAY)
img_edge = cv.Canny(img_gray, 100, 300)

# 원본 컬러 영상에 다시 ROI를 복사하기 위해 컬러 영상으로 변환합니다.
img_edge = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)

# 원본 컬러 영상에 다시 ROI를 복사해줍니다.
img_color[center_y-100:center_y+100, center_x-100:center_x+100] = img_edge

cv.imshow("COLOR", img_color)
cv.imshow("ROI", img_roi)

cv.waitKey(0)

cv.destroyAllWindows()