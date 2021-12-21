import RPi.GPIO as GPIO
import time

j=1
BUZZER_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [392,392,440,440,392,392,329.6,392,392,329.6,329.6,293.6
,392,392,440,440,392,392,329.6,392,329.6,293.6,329.6,261.6]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        if (j==7 or j==19):
            time.sleep(1)
        elif (j==12 or j==24):
            time.sleep(1.5)
        time.sleep(0.5)
        j = j + 1

finally:
    pwm.stop()
    GPIO.cleanup()