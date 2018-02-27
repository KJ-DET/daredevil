import time
from RPi import GPIO
from config import settings
from hardware import Hardware

class DistanceSensor(Hardware):
   
    def __init__(self,name, GPIO_ECHO,GPIO_TRIG):
        self.name = name
        self.GPIO_ECHO = GPIO_ECHO
        self.GPIO_TRIG = GPIO_TRIG

        print "Initialzing DistanceSensor::" , self.name 
        print "EchoPin is " , self.GPIO_ECHO
        print "Trigger Pin is ", self.GPIO_TRIG

        GPIO.setup(self.GPIO_ECHO,GPIO.IN)
        GPIO.setup(self.GPIO_TRIG,GPIO.OUT)
        GPIO.output(self.GPIO_TRIG,False)
        print "reseting trigger"
        time.sleep(2)

    def send_soundwave(self):
        print "Sending Soundwave for ::" ,self.name
        GPIO.output(self.GPIO_TRIG,True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIG,False)

    def get_pulse_duration(self):
        print "Getting pulse duration for ::" ,self.name
        start_time = time.time()

        while GPIO.input(self.GPIO_ECHO)==0:
            start_time = time.time()

        while GPIO.input(self.GPIO_ECHO)==1:
            stop_time = time.time()
        
        time_taken = stop_time - start_time
        return time_taken

    def compute_distance(self,duration):
        print "Computing distance for ::" ,self.name
        d = 34300*duration/2
        print self.name, 'distance=', d
        return d

    def get_distance(self):
        print "Getting distance for ::" ,self.name

        self.send_soundwave()
        duration = self.get_pulse_duration()
        return self.compute_distance(duration)	 

    def measure_distance(self):
        print "Measuring distance"

        GPIO.output(self.GPIO_TRIG,True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIG,False)
        start_time = time.time()

        while GPIO.input(self.GPIO_ECHO)==0:
            start_time = time.time()

        while GPIO.input(self.GPIO_ECHO)==1:
            stop_time = time.time()
        
        time_taken = stop_time - start_time
        distance = (time_taken*34300)/2

        print self.name , 'distance=' , distance

        return distance

    
