import RPi.GPIO as GPIO
import time

REDLED_PIN = 13
REDSWITCH_PIN = 21
YELLOWLED_PIN = 6
YELLOWSWITCH_PIN = 20
GREENLED_PIN = 5
GREENSWITCH_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(REDLED_PIN, GPIO.OUT)
GPIO.setup(REDSWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(YELLOWLED_PIN, GPIO.OUT)
GPIO.setup(YELLOWSWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GREENLED_PIN, GPIO.OUT)
GPIO.setup(GREENSWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
       rval = GPIO.input(REDSWITCH_PIN)
       yval = GPIO.input(YELLOWSWITCH_PIN)
       gval = GPIO.input(GREENSWITCH_PIN) #누르지 않은 경우 0, 누른 경우 1
       print(rval)
       print(yval)
       print(gval)

       GPIO.output(REDLED_PIN, rval) # GPIO.HIGH (1), GPIO.LOW (0)
       GPIO.output(YELLOWLED_PIN, yval)
       GPIO.output(GREENLED_PIN, gval)
       time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')