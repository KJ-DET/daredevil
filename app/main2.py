from hardware.hardware import Board
from core import distance

board = Board()
try:
    distance.print_distance()
except KeyboardInterrupt:
    board.destroy()
