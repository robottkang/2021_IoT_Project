import RPi.GPIO as GPIO
import time

#              A  B  C   D   E   F   G
SEGMENT_PIN = [6, 5, 13, 19, 20, 21, 26]
LED_PIN = 23
TRIG_PIN = 17
ECHO_PIN = 18
#7 segment로 나타나는 숫자
#       1               2               3               4               5               6               7               8               9
data = [[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,0,0,1,1]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

for segment in SEGMENT_PIN:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

try:
    while True:
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001) # 10us (microsec)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0: #펄스 발생 중
            pass
        start = time.time() #ECHO PIN HIGH (시작)

        while GPIO.input(ECHO_PIN) == 1: #펄스 발생 종료
            pass
        stop = time.time() #ECHO PIN LOW (종료)

        duration_time = stop - start
        distance = duration_time * 17160 #distance의 단위를 cm로 설정

        print('distance : %.1fcm' % distance)

        if distance <= 600:
            GPIO.output(LED_PIN, 1) #거리가 6m이하면 LED 발광 초과면 LED 소등
        elif distance >600:
            GPIO.output(LED_PIN, 0)
        
        if distance <= 50:                             # 1 : 50cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[0][i])
        elif 50<distance <= 100:                       # 2 : 50cm초과 100cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[1][i])
        elif 100<distance <= 300:                      # 3 : 100cm초과 300cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[2][i])
        elif 300<distance <= 600:                      # 4 : 300cm초과 600cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[3][i])
        elif 600<distance <= 1000:                     # 5 : 600cm초과 1000cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[4][i])
        elif 1000<distance <= 1500:                    # 6 : 1000cm초과 1500cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[5][i])
        elif 1500<distance <= 2100:                    # 7 : 1500cm초과 2100cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[6][i])
        elif 2100<distance <= 2800:                    # 8 : 2100cm초과 2800cm이하
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[7][i])
        elif 2800<distance:                            # 9 : 2800cm초과
            for i in range(len(SEGMENT_PIN)):
                GPIO.output(SEGMENT_PIN[i], data[8][i])
        else: continue

finally: #종료
    GPIO.cleanup()
    print('cleanup and exit')