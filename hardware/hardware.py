
from config import settings
from RPi import GPIO

class Board(object):
    '''
    Global things
    '''
    def __init__(self):
        if settings.PIN_SCHEME == "BOARD":
            GPIO.setmode(GPIO.BOARD)    
        else:
            GPIO.setmode(GPIO.BCM)    

    def destroy(self):
        GPIO.cleanup()

class Hardware(object):
    '''
    Base class for all hardware classes. All hardware classes must inherit from this class.
    '''
    def init(self):
        pass           


