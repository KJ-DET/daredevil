
from hardware.hardware import Board
from core import lights

board = Board()
lights.blink_5_times()
board.destroy()
