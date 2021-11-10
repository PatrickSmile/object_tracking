import cv2 as cv

# Contour 영역 내에 텍스트를 쓰기 위해 사용합니다.
def setLabel(image, str, contour):

    (text_width, text_height), baseline = cv.getTextSize(str, cv.FONT_HERSHEY_SIMPLEX)

    x,y,width,height = cv.boundingRect(contour)

    pt_x = x + int((width - text_width)/2)
    pt_y = y + int((height + text_height)/2)

    cv.rectangle(image, (pt_x, pt_y + baseline), (pt_x, + ))