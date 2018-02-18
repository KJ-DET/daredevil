import time
from RPi import GPIO
from config import settings
from hardware import Hardware

class DistanceSensor(Hardware):
   
    def __init__(self,name, echo_pin,trigger_pin):
        self.name = name
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin

        print "Initialzing DistanceSensor::" , self.name 
        print "EchoPin is " , self.echo_pin
        print "Trigger Pin is ", self.trigger_pin

        GPIO.setup(self.echo_pin,GPIO.IN)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.output(self.trigger_pin,False)
        print "reseting trigger"
        time.sleep(2)
        
    def measure_distance(self):
        print "Measuring distance"

        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin,False)
        start_time = time.time()

        while GPIO.input(self.echo_pin)==0:
            start_time = time.time()

        while GPIO.input(self.echo_pin)==1:
            stop_time = time.time()
        
        time_taken = stop_time - start_time
        distance = (time_taken*34300)/2

        return distance

    
