import cv2 as cv

cap = cv.VideoCapture(0)

if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

# 캡처된 이미지의 크기를 확인하기 위해 이미지 1장을 캡처합니다.
ret, img_frame = cap.read()

if ret == False:
    print("캡처실패")
    exit(1)

# 동영상 파일을 위한 코덱을 설정합니다.
codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G');

# 프레임 레이트(Frame rate)를 설정합니다.
fps = 30.0

# 이미지 크기를 가져옵니다.
h,w = img_frame.shape[:2]

# 동영상 파일을 저장하려면 VideoWriter 객체를 생성해야합니다.
# VideoWriter 객체를 초기화하기 위해 저장할 동영상 파일 이름,
# 코덱, 프레임레이트, 이미지 크기를 지정합니다.
writer = cv.VideoWriter("output.avi", codec, fps, (w,h))

# VideoWriter 객체를 성공적으로 초기화했는지 체크합니다.
if writer.isOpened() == False:
    print("동영상 파일을 준비할 수 없습니다.")
    exit(1)

# ESC 키를 눌러서 카메라 앱을 종료하면 종료 직전까지
# 카메라가 찍은 연속 이미지가 동영상으로 저장됩니다.
while(True):

    # 카메라에서 이미지를 캡처합니다.
    ret, img_frame = cap.read()

    if ret == False:
        print("캡처 실패")
        break;

    # 캡처한 이미지를 동영상 파일에 추가합니다.
    writer.write(img_frame)

    cv.imshow('Color', img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()

# 동영상 저장을 완료하기 위해 VideoWriter 객체를 릴리즈합니다.
writer.release();

cv.destroyAllWindows()

