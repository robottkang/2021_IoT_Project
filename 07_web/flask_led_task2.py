from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN1 = 5
LED_PIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("led2.html")

@app.route("<color>/led/<op>")
def led_op(color, op):
    if color == "RED":
        if op == "on":
            return GPIO.output(LED_PIN1, GPIO.HIGH)
        elif op == "off":
            return GPIO.output(LED_PIN1, GPIO.LOW)
    elif color == "BLUE":
        if op == "on":
            return GPIO.output(LED_PIN2, GPIO.HIGH)
        elif op == "off":
            return GPIO.output(LED_PIN2, GPIO.LOW)

try:
    if __name__ == "__main__":
        app.run(host="0.0.0.0")

finally:
    GPIO.cleanup()
    print("Cleanup and exit")