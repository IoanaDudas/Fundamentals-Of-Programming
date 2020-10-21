from board import Board


class GameWonException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class GameDrawException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Game:
    def __init__(self, board, algorithm):
        self._board = board
        self._algorithm = algorithm

    def playerMove(self, column):
        self._board.move(column, 'Y')

    def computerMove(self):
        column = self._algorithm.nextMove(self._board)
        self._board.move(column, 'R')

    def check(self):
        if self._board.isWon('Y') == True or self._board.isWon('R') == True:
            raise GameWonException("")
        if self._board.isTie() == True:
            raise GameDrawException("")

    def getBoard(self):
        return self._board