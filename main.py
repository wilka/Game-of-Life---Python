import sys
from time import sleep
import pygame
import pygame.display as display
import pygame.draw as draw
from gameBoard import GameBoard

pygame.init()

cellSize = 25,25
gridSize = 50,40


black = 0, 0, 0


display.set_caption("Game of Life")
screenSize = width, height = gridSize[0] * cellSize[0], gridSize[1] * cellSize[1]
screen = display.set_mode(screenSize)

board = GameBoard(gridSize)

# Glider at the top left
board.setCell((1, 0), True)
board.setCell((2, 1), True)
board.setCell((0, 2), True)
board.setCell((1, 2), True)
board.setCell((2, 2), True)

# Blinker at the top middle
board.setCell((20, 2), True)
board.setCell((20, 3), True)
board.setCell((20, 4), True)


def drawCell(surface, position):
    cellMainColor = 180, 180, 180
    cellLightEdgeColor = 220, 220, 220
    cellDarkEdgeColor = 120, 120, 120

    (x, y) = position
    (cellWidth, cellHeight) = cellSize

    x *= cellWidth
    y *= cellHeight

    draw.rect(surface, cellMainColor, ((x, y), cellSize))
    draw.line(surface, cellLightEdgeColor, (x,y), (x, y + cellHeight))
    draw.line(surface, cellLightEdgeColor, (x,y), (x + cellWidth, y))
    draw.line(surface, cellDarkEdgeColor, (x, y + cellHeight), (x + cellWidth, y + cellHeight))
    draw.line(surface, cellDarkEdgeColor, (x + cellWidth, y), (x + cellWidth, y + cellHeight))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    for (x, row) in enumerate(board.board):
        for (y, isAlive) in enumerate(row):
            if isAlive:
                drawCell(screen, (x,y))

    pygame.display.flip()

    board = board.nextGeneration()

    sleep(0.25)