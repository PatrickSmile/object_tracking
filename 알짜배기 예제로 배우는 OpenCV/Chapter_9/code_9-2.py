import cv2

img_color = cv2.imread('cat.jpg')
cv2.imshow("color", img_color)

height,width = img_color.shape[:2]

# 이미지 중앙을 중심으로 반시계 방향으로 45도 회전시키는 행렬을 생성합니다.
M = cv2.getRotationMatrix2D(
    (width/2.0, height/2.0), #회전할때의 중심점
    45, # 회전 각도(양수 반시계 방향, 음수 시계방향)
    1
    ) # 이미지 배율, 1이면 원래 크기

# 회전 행렬 M을 이미지 img_color에 적용합니다.
img_rotated = cv2.warpAffine(img_color, M, (width, height))

cv2.imshow("rotation", img_rotated)
cv2.waitKey(0)

cv2.destroyAllWindows()

