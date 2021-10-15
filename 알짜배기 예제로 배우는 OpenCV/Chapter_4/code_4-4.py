import cv2 as cv
import sys

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    sys.exit(1)

# 보여줄 결과를 지정하기 위해 사용하는 변수입니다.
step = 1

while(True):

    # img_grame 변수에 대입된 이미지를 윈도우에 보여주게 됩니다.
    # 처음에는 카메라에서 캡처된 컬러 이미지입니다.
    ret, img_frame = cap.read()

    if ret == False:
        print("캡처 실패")
        break;

    # step이 2 이상이면 img_frame에는 그레이 스케일 이미지가 대입됩니다.
    if step > 1:
        img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

        # step이 3이 되면 img_frame에는 에지 이미지가 대입됩니다.
        if step >2:
            img_frame = cv.Canny(img_frame, 30, 90)


    # 앞에서 처리된 결과에 따라 다른 이미지가
    # Result 윈도우에 보여지게 됩니다.
    cv.imshow('Result', img_frame)

    # 1초 동안 키보드 입력을 대기합니다.
    key = cv.waitKey(1)

    if key == 27: # ESC키
        break

    # 입력된 키에 따라 step 변수에 다른 값을 대입합니다.
    # Python에서는 ord함수를 사용하여 문자를 ASCII 코드로
    # 변환할 수 있습니다.

    elif key == ord('1'):
        step = 1
    elif key == ord('2'):
        step = 2
    elif key == ord('3'):
        step = 3


cap.release()
cv.destroyAllWindows()