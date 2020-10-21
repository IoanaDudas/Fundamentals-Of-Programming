from game import *
from algorithm import *
from board import *
import pygame
import sys
import math

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

pygame.init()

squareSize = 100
width = 7 * squareSize
height = 7 * squareSize
radius = int(squareSize/2 - 5)
size = (width, height)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("comicsansms", 65)

board = Board()

def drawBoard(board):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, blue, (c * squareSize, r * squareSize+squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, black, (int(c * squareSize+squareSize/2), int(r * squareSize+squareSize+squareSize/2)), radius)
    for c in range(7):
        for r in range(6):
            if board.get(r, c) == 1:
                pygame.draw.circle(screen, yellow, (int(c * squareSize + squareSize / 2),
                                                    int(r * squareSize + squareSize + squareSize / 2)), radius)
            elif board.get(r, c) == -1:
                pygame.draw.circle(screen, red, (int(c * squareSize + squareSize / 2),
                                                    int(r * squareSize + squareSize + squareSize / 2)), radius)
    pygame.display.update()


drawBoard(board)
pygame.display.update()

class GUI:
    def __init__(self, game):
        self._game = game

    def start(self):
        board = self._game.getBoard()
        playerMove = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, black, (0, 0, width, squareSize))
                    posX = event.pos[0]
                    #if playerMove == True:
                    pygame.draw.circle(screen, yellow, (posX, int(squareSize/2)), radius)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        playerMove = True
                        posX = event.pos[0]
                        column = int(math.floor(posX/squareSize))
                        self._game.playerMove(column)
                        self._game.check()
                        playerMove = not playerMove
                        self._game.computerMove()
                        self._game.check()
                    except GameWonException:
                        if playerMove == True:
                            print(board)
                            drawBoard(board)
                            label = myfont.render("Congrats, you won!", 1, green)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            pygame.time.wait(3000)
                        else:
                            print(board)
                            drawBoard(board)
                            label = myfont.render("You lost!", 1, green)
                            screen.blit(label, (40, 5))
                            pygame.display.update()
                            pygame.time.wait(3000)
                        return
                    except GameDrawException:
                        print(board)
                        drawBoard(board)
                        label = myfont.render("Game is draw!", 1, green)
                        screen.blit(label, (40, 5))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        return
                    except ValueError:
                        continue
                print(board)
                drawBoard(board)
