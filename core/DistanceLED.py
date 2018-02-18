
import time
from hardware.led import LED
from hardware.distanceSensor import DistanceSensor


def loop():
    rightS = DistanceSensor("RightSensor",18,4)
    centerS = DistanceSensor("LeftSensor",23,17)

    led = LED(27)

    while True:
        if rightS.measure_distance() < 50 :
            led.blink(count=2)
        if centerS.measure_distance() < 50 :
            led.blink(count=1)
        time.sleep(1)  

