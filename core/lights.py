
import time
from hardware.led import LED

def blink_once():
    print "inside blink_once"
    led_1 = LED(12)
    led_1.blink()

def blink_5_times():
    print "inside blink_once"
    led_1 = LED(12)
    led_1.blink(count=5)
