import cv2

img_gray = cv2.imread('house.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', img_gray)

# 블러링을 적용한 후, 캐니 에지 디텍터를 적용합니다.
img_gray = cv2.blur(img_gray, (3,3))
# 보통 첫 번째 임계값의 2~3배로 두 번째 임계값을 정합니다.
img_canny = cv2.Canny(img_gray, 50, 150)
cv2.imshow('Canny Edge', img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()