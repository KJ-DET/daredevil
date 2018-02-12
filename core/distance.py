from hardware.ultrasonic import Ultrasonic
import time

def print_distance():
    distanceSensor = Ultrasonic(21,17)
    while(True):
        #pdistanceSensor.get_distances()
        print "Distance is ::" , distanceSensor.distance()
        time.sleep(1)

#    while(True):
#        distanceSensor = Ultrasonic(21,17,1,0.5)
#        print "Distance is ::" , distanceSensor.distance()
 #       sleep(1)
      #  distanceSensor.wait_for_out_of_range(1)


