
from hardware.hardware import Board
#from core import lights
#from core import DistanceLED
from core import DistanceMotor

try:
    board = Board()
    #lights.blink_5_times()
    #DistanceLED.loop()
    DistanceMotor.loop()
    
except KeyboardInterrupt:
    board.destroy()
