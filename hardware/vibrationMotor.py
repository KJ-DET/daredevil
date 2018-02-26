from config import settings
from hardware import Hardware
from RPi import GPIO
import time as time

class VibrationMotor(Hardware):
    def __init__(self,name,GPIO_MOTOR):
        self.name = name
        self.GPIO_MOTOR = GPIO_MOTOR
        print 'Initializing Vibration Motor'
        GPIO.setup(self.GPIO_MOTOR,GPIO.OUT)
        GPIO.output(self.GPIO_MOTOR,GPIO.LOW)
        time.sleep(2)

    def motor_on(self):
        GPIO.output(self.GPIO_MOTOR,GPIO.HIGH)

    def motor_off(self):
        GPIO.output(self.GPIO_MOTOR,GPIO.LOW)

    def vibrate_slow(self):
        self.motor_on()
        time.sleep(0.15)
        self.motor_off()
        time.sleep(0.5)
        
    def vibrate_fast(self):
        self.motor_on()
        time.sleep(0.5)
        self.motor_off()
        time.sleep(0.15)
