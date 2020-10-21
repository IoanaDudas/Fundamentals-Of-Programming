from board import Board

import random
class MoveAlgorithm1:
    # take the first unocupied square
    def nextMove(self, board):
        # Return the computers next move
        candidates = []
        for i in range(6):
            for j in range(7):
                if board.get(i,j) == 0:
                    candidates.append((i,j))
        choice = random.choice(candidates)
        return choice[1]

class MoveAlgorithm2:
    # take the first unocupied square
    def nextMove(self, board):
        # Return the computers next move
        candidates = []
        for i in range(6):
            for j in range(7):
                if board.get(i,j) == 0:
                    candidates.append((i,j))
        for i in range(6):
            sum = 0
            for j in range(7):
                if board.get(i,j) == 1:
                    sum += 1
                if sum == 1:
                    choice = (i,j+1)
                else:
                    choice = random.choice(candidates)
        for j in range(7):
            sum = 0
            for i in range(6):
                if board.get(i,j) == 1:
                    sum += 1
                if sum == 1:
                    choice = (i+1,j)
                else:
                    choice = random.choice(candidates)
        return choice[1]