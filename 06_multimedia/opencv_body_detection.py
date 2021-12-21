import cv2
import RPi.GPIO as GPIO
import time
#필요한 것들 임포트해주기

PIR_PIN = 15
LED_PIN = 14
BUZZER_PIN = 13

SEGMENT_PINS1 = [2, 3, 4, 5, 6, 7]
SEGMENT_PINS2 = [8, 9, 10, 11, 12]

alarm = [261,392]

# 사용할 cascade xml 파일 선택
body_cascade = cv2.CascadeClassifier('./xml/haarcascade_fullbody.xml')
# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 핀 번호 설정하기
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_UP)
# 핀 모드 설정하기
for segment1 in SEGMENT_PINS1:
    GPIO.setup(segment1, GPIO.OUT)
    GPIO.output(segment1, GPIO.LOW)
    # segment1 GPIO.LOW로 바꾸기
for segment2 in SEGMENT_PINS2:
    GPIO.setup(segment2, GPIO.OUT)
    GPIO.output(segment2, GPIO.LOW)
    # segment2 GPIO.LOW로 바꾸기


time.sleep(4)
print('경보기 작동을 시작합니다.')
#경보기 작동 시작하기

pwm = GPIO.PWM(BUZZER_PIN, 392)
pwm.start(10)
# 버저 핀 솔 음으로 설정하기

try:
    while True:
        # 한 프레임 받아오기
        ret, frame = cap.read()
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:  #움직임 결과가 1, 움직임이 감지되면
            print("움직임이 감지되었습니다.")
            # 이미지를 회색으로 변환
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # 이미지에서 몸 검출
            body = body_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(body) >= 1:   #몸이 감지가 되면
                for (x, y, w, h) in body: # 몸에대한 위치 정보 가져오기
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
                cv2.imshow('frame', frame)
                
                print('사람이 감지되었습니다. 경보기 작동을 시작합니다.')
                cv2.imwrite('person.jpg', frame)
                print('사진을 촬영하였습니다.')
                GPIO.output(LED_PIN, GPIO.HIGH)
                for i in range(6):  # 0~5
                    GPIO.output(SEGMENT_PINS1[i], GPIO.HIGH) #세그먼트 점등하기
                for i in range(5):  # 0~4
                    GPIO.output(SEGMENT_PINS2[i], GPIO.HIGH) #세그먼트 점등하기
                for _ in range(3):  # 버저 3번 작동
                    for i in alarm: # 도, 솔 음 재생
                        pwm.ChangeFrequency(i) # 버저 음 변경
                        pwm.ChangeDutyCycle(100)    #버저 작동
                        time.sleep(0.5)
                        pwm.ChangeDutyCycle(0)      #버저 작동 중지
                        time.sleep(0.5)
        else:                 #움직임 결과가 0, 움직임이 감지되지 않으면
            print('움직임이 감지되지 않았습니다.')
            GPIO.output(LED_PIN, GPIO.LOW)
            for k in range(6):
                GPIO.output(SEGMENT_PINS1[k], GPIO.LOW)      #세그먼트 소등하기
            for l in range(5):
                GPIO.output(SEGMENT_PINS2[l], GPIO.LOW)      #세그먼트 소등하기
            pwm.ChangeDutyCycle(0)
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == 27:
            break
        time.sleep(0.1)


finally:        #정지했을 때
    pwm.stop()
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    print('경보기 작동을 중지합니다.')