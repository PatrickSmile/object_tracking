# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#필요한 OpenCV 패키지를 임포트합니다.
import cv2

# 첫 번째 아규먼트로 지정한 파일을 컬러 포맷으로 불러옵니다.
# IMREAD_COLOR는 컬러포맷으로 영상을 읽겠다는 의미입니다.
# 이미지를 img_color변수에 넘파이 배열로 대입됩니다.
img_color = cv2.imread("cat on laptop.jpg", cv2.IMREAD_COLOR)

# 이미지를 불러올 수 없으면 img_color 뱐슨,ㄴ None(값없음)이 됩니다.
# 이미지 불러올 수 없는 경우를 체크하기 위해 사용합니다.
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

# 이미지를 보여줄 윈도우를 생성합니다.
# 첫 번째 아규먼트로 윈도우 식별자로 사용할 문자열을 지정해줍니다.
# 지정한 문자열이 윈도우의 타이틀바에 보이게 됩니다.
cv2.namedWindow('Color')

# 윈도우 식별자가 "Color"인 윈도우에 변수 img_color가
# 가리키는 넘파이 배열에 저장된 이미지를 보여줍니다.
# 대부분의 경우 namedWindows를 생략하고 imshow만 사용해도
# 윈도우에 이미지를 보여줍니다.
cv2.imshow('Color', img_color)

# ms 단위로 지정한 시간만큼 대기합니다.
# 0이면 OpenCV로 생성한 윈도우 창이 선택된 상태에서
# 키보드 입력이 있을 때까지 대기합니다.
cv2.waitKey(0)

#사용이 끝난 윈도우를 종료해줍니다.
cv2.destroyAllWindows()