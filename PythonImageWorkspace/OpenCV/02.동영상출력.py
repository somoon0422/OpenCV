## 동영상출력 

#1. 동영상 파일 출력 
import cv2

cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("더이상 가져올 프레임이 없어요")
        break
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(25) == ord('q'):
        print('사용자 입력에 의해 종료합니다')
        break
cap.release() #자원해제
cv2.destroyAllWindows() #모든 창 닫기


    
