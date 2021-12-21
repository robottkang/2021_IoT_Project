import drivers
import Adafruit_DHT
import time
import datetime

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    print("Writing to display")
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%x %X"))
        display.lcd_display_string(now.strftime("%x%X"), 1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            print(f"{temperature:.1f}C, {humidity:.1F}%")
            display.lcd_display_string(f"{temperature:.1f}C, {humidity:.1F}%", 2)
        else:
            print('Read error')

finally:
    print("Cleaning up!")
    display.lcd_clear()