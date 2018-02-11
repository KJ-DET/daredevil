from gpiozero import DistanceSensor as gzDistanceSensor
from config import settings
from hardware import Hardware

class Ultrasonic(Hardware):
    def __init__(self,echo_pin,trigger_pin,max_distance,threshold_distance):
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin
        print "Setting Echo Pin at " , echo_pin
        print "Setting Trigger Pin at " trigger_pin
        self.gzDistanceSensor = DistanceSensor(echo_pin,trigger_pin,max_distance,threshold_distance)
#        self.gzDistanceSensor.max_distance =1
#        self.gzDistanceSensor.threshold_distance = 0.
    def max_distance(max_distance):
        print "Setting Maximum Distance Range as " , max_distance

        self.gzDistanceSensor.max_distance = max_distance

    def threshold_distance(threshold):
        print "Setting Threshold Distance as " , threshold

        self.gzDistanceSensor.threshold_distance = threshold_distance

    def measure_distance():
        return self.gzDistanceSensor.distance

