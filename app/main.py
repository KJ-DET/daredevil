
from hardware.hardware import Board
from core import lights
from core import DistanceLED.py

try:
    board = Board()
#lights.blink_5_times()
    DistanceLEd.loop()
    
except KeyboardInterrupt:
    board.destroy()
