
from RPi import GPIO
from config import settings
from hardware import Hardware

class LED(Hardware):
    def __init__(self, led_pin):
        led_pin = led_pin
        GPIO.setup(led_pin, GPIO.OUT)      
    def on(self):
        GPIO.output(led_pin, GPIO.HIGH)
    def off(self):
        GPIO.output(led_pin, GPIO.HIGH)
    def blink(self):
        pass

