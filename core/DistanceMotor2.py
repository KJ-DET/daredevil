import time as time
#from hardware.led import LED
from hardware.distanceSensor import DistanceSensor
from hardware.vibrationMotor import VibrationMotor


def loop():
    leftS = DistanceSensor("LeftSensor",25,4)
    centerS = DistanceSensor("CenterSensor",23,17)
    rightS = DistanceSensor("RightSensor",22,24)
    leftM = VibrationMotor("LeftMotor", 18)
    rightM = VibrationMotor("RightMotor", 12)

#    led = LED(27)

    while True:
        ld = leftS.get_distance()
        rd = rightS.get_distance()
        cd= centerS.get_distance()

        if ld <=50 and rd <=50 and cd <=50 :
            leftM.vibrate_fast() 
            rightM.vibrate_fast()
        elif ld <=50 and rd <= 50:
            leftM.vibrate_slow()
            rightM.vibrate_slow()
        elif rd() <= 50 and cd <=50:
            rightM.vibrate_fast()
        elif ld() <= 50 and cd <=50:
            leftM.vibrate_fast()
        elif rd <= 50:
            rightM.vibrate_slow()
        elif ld <= 50:
            leftM.vibrate_slow()
        elif cd <= 50:
            leftM.vibrate_continous()
        else
            leftM.off()
            rightM.off()
        time.sleep(1)
    
    #while True:
     #   if rightS.measure_distance() < 50 :
      #      led.blink(count=2)
       # if centerS.measure_distance() < 50 :
        #    led.blink(count=1)
        #time.sleep(1)  

