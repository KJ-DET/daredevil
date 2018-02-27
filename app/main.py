
from hardware.hardware import Board
#from core import lights
#from core import DistanceLED
from core import DistanceMotor2

try:
    board = Board()
    #lights.blink_5_times()
    #DistanceLED.loop()
    #DistanceMotor.loop()
    DistanceMotor2.loop()
    
except KeyboardInterrupt:
    board.destroy()
