import cv2 as cv
import numpy as np

# 새로운 좌표와 근사한 좌표가 기존 리스트에 있는지 체크합니다.
def notInList(newObject):
    for detectedObject in detectedObjects:
        a = newObject[0] - detectedObject[0]
        b = newObject[1] - detectedObject[1]
        if np.sqrt(a*a + b*b) < 5:
            return False
    return True

detectedObjects=[]

img_rgb = cv.imread('test.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
img_template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)

# 임계값 0.9보다 크고
# 기존에 템플릿 검출 리스트에 포함된 좌표와 거리가 5 이상이어야
# 새로운 좌표 리스트에 추가합니다.
count = 0
for x in range(res.shape[1]):
    for y in range(res.shape[0]):
        if res[y, x] > 0.9 and notInList((x,y)):
            detectedObjects.append((x,y))
            cv.rectangle(img_rgb, (x,y), (x+w, y+h), [0,0,255], 1)
            count = count + 1

print(count)
cv.imshow('result', img_rgb)
cv.waitKey(0)