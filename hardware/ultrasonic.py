from gpiozero import DistanceSensor as gzDistanceSensor
from config import settings
from hardware import Hardware

class Ultrasonic(Hardware):
    def __init__(self,echo_pin,trigger_pin):#,max_distance,threshold_distance):
        #self.echo_pin = echo_pin
        #self.trigger_pin = trigger_pin
        print "Setting Echo Pin at " , echo_pin
        print "Setting Trigger Pin at ", trigger_pin
        self.gzDistanceSensor = gzDistanceSensor(echo_pin,trigger_pin)#,max_distance,threshold_distance)

    def max_distance(self,max_distance):
        print "Setting Maximum Distance Range as " , max_distance

        self.gzDistanceSensor.max_distance = max_distance

    def threshold_distance(self,threshold):
        print "Setting Threshold Distance as " , threshold

        self.gzDistanceSensor.threshold_distance = threshold_distance

    def distance(self):
        return self.gzDistanceSensor.distance * 100

    def wait_for_out_of_range(self):
        print "Going out of range"
        self.gzDistanceSensor.wait_for_out_of_range()

    def wait_for_in_range(self):
        print "Coming in range"
        self.gzDistanceSensor.wait_for_in_range()

    def get_distances(self):
        while self.wait_for_in_range():
            print "Distance is:: " , self.distance()



