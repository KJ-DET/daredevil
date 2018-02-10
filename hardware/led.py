
import time
from RPi import GPIO
from config import settings
from hardware import Hardware

class LED(Hardware):
    def __init__(self, led_pin):
        self.led_pin = led_pin
        print "led_pin", led_pin
        print "GPIO.setup(self.led_pin, GPIO.OUT)"
        GPIO.setup(self.led_pin, GPIO.OUT)      
        GPIO.output(self.led_pin, False)
    def on(self):
        print "GPIO.output(self.led_pin, GPIO.HIGH)"
        GPIO.output(self.led_pin, GPIO.HIGH)
    def off(self):
        print "GPIO.output(self.led_pin, GPIO.LOW)"
        GPIO.output(self.led_pin, GPIO.LOW)
    def blink(self, count=1, on_duration_sec=1, off_duration_sec=1):
        for i in range(count):
            self.on()
            time.sleep(on_duration_sec)
            self.off()
            time.sleep(off_duration_sec)
