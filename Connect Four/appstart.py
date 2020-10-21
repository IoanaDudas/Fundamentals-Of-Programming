from game import *
from algorithm import *
from board import *
from ui import *
from gui import *

board = Board()
alg = MoveAlgorithm1()
game = Game(board, alg)
ui = GUI(game)
ui.start()