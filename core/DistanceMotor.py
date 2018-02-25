
import time as time
from hardware.led import LED
from hardware.distanceSensor import DistanceSensor
from hardware.vibrationMotor import VibrationMotor


def loop():
    leftS = DistanceSensor("LeftSensor",25,4)
    centerS = DistanceSensor("CenterSensor",23,17)
    rightS = DistanceSensor("RightSensor",22,24)
    leftM = VibrationMotor("LeftMotor", 18)
    rightM = VibrationMotor("RightMotor" 12)

    led = LED(27)

    while True:
        if leftS.get_distance() <=50 :
            leftM.vibrate_slow()
        if rightS.get_distance() <= 50:
            rightM.vibrate_slow()
        if centerS.get_distance() <=50:
            leftM.vibrate_fast() 
            rightM.vibrate_fast()
    
    #while True:
     #   if rightS.measure_distance() < 50 :
      #      led.blink(count=2)
       # if centerS.measure_distance() < 50 :
        #    led.blink(count=1)
        #time.sleep(1)  

