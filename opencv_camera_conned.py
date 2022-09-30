# 카메라 연결 코드

import cv2 # openCV 2 라이브러리


# openCV Python
# 카메라 영상을 받아올 개게 선언 및 설정(영상 소스, 해상도 설정)

cap = cv2.VideoCapture(0) # cap이라는 객체를 선언 후, 0번 웹캠으로부터 영상을 가져온다는 뜻이다

# 해상도 크기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # 너비
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # 높이

# 무한루프

while True:
    ret, frame = cap.read() # 카메라로부터 현재 영상을 받아 frame에 저장하고 잘 받았으면 ret이 참이다
    cv2.imshow("original", frame) # frame(카메라 영상)을 original 이라는 창에 띄워준다
    if cv2.waitKey(1) == ord('q'): # 키보드의 q를 누르면 무한루프가 멈춘다
        break
    
cap.release() # 캡처 객체를 없애준다
cv2.destroyAllWindows() # 모든 영상 창을 닫아준다
