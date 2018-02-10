
from hardware.hardware import Board
from core import lights

board = Board()
lights.blink_once()
board.destroy()
