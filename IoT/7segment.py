import RPi.GPIO as GPIO
import time

SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

# Common Cathode : ON -> HIGH, OFF -> LOW
data = [1, 1, 1, 1, 1, 1, 0]
many_data = [[1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]
        [1, 1, 1, 1, 1, 1, 0]]



try:
    for i in range(3): # 0~2
        for j in range(7): #0~6
            GPIO.output(SEGMENT_PINS[j], data[j])

        time.sleep(1)

        for j in range(7):
            GPIO.output(SEGMENT_PINS[j], GPIO.LOW)

finally:
    GPIO.cleanup()
    print("cleanup and exit")