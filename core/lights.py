
import time
from hardware.led import LED

def blink_once():
    print "inside blink_once"
    led_1 = LED(12)

    led_1.on()
    time.sleep(30)
    led_1.off()
