import RPi.GPIO as GPIO
import time

LEDR = 22
LEDY = 23
LEDG = 24
GPIO.setmode(GPIO.BCM)      # GPIO.BCM or GPIO.BOARD
GPIO.setup(22, GPIO.OUT)   # GPIO.OUT or GPIO.IN
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

for i in range(10):   
    GPIO.output(LEDR, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(LEDR, GPIO.LOW)  #0
    print("led off")
    GPIO.output(LEDY, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(LEDY, GPIO.LOW)  #0
    print("led off")
    GPIO.output(LEDG, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(LEDG, GPIO.LOW)  #0
    print("led off")
    

GPIO.cleanup()              # GPIO 핀상태 초기화