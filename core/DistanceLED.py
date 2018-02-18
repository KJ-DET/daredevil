
import time
from hardware.led import LED
from hardware.distanceSensor import DistanceSenosr


def loop():
    rightS = DistanceSensor("RightSensor",18,4)
    leftS = DistanceSensor("LeftSensor",23,17)

    led = LED(27)

    while True:
        if rightS.measure_distance() < 50 :
            led.blink(count=2)
        if leftS.measure_distance() < 50 :
            led.blink(count=1)
        time.sleep(1)  

