import cv2 as cv

alpha = 0.0
beta = 1.0

while alpha <= 1.0:

    # addWeighted 파라미터 조정 효과를 확인하기 위해
    # 루프 시작할 때마다 이미지를 새로 불러옵니다.
    # 블렌딩하는 두 이미지의 크기는 같아야 합니다.
    img1 = cv.imread("beach.png", cv.IMREAD_COLOR)
    img2 = cv.imread("cat.png", cv.IMREAD_COLOR)

    # addWeighted함수를 사용하여 블렌딩을 적용합니다.
    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    # 블렌딩을 위해 사용한 파라미터를 확인합니다.
    print( alpha, " ", beta)

    # 결과 이미지를 화면에 보여줍니다.
    cv.imshow('dst', dst)
    cv.waitKey(0)

    # img1을 위한 가중치 alpha는 0.1씩 증가시키고
    # img2를 위한 가중치 beta는 0.1씩 감소시킵니다.
    # img2 이미지는 점점 투명해지고, img1 이미지는 점점 불투명해집니다.
    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)

cv.destroyAllWindows()