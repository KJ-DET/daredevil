from hardware.ultrasonic import ultrasonic

def print_distance():

    while(True):
        distanceSensor = ultrasonic(21,17,1,0.5)
        print "Distance is ::" + distanceSensor.measure_distance()

