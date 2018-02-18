
from hardware.hardware import Board
from core import lights
from core import DistanceLED

try:
    board = Board()
    #lights.blink_5_times()
    DistanceLED.loop()
    
except KeyboardInterrupt:
    board.destroy()
