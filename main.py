import sys
import pygame
import pygame.display as display
import pygame.draw as draw

pygame.init()

cellSize = 25,25
gridSize = 50,40


black = 0, 0, 0


display.set_caption("Game of Life")
screenSize = width, height = gridSize[0] * cellSize[0], gridSize[1] * cellSize[1]
screen = display.set_mode(screenSize)


board = []
for x in range(gridSize[0]):
    row = []
    for y in range(gridSize[1]):
        row.append(False)
    
    board.append(row)


board[0][0] = True
board[1][1] = True
board[1][9] = True
board[20][1] = True


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

    for (x, row) in enumerate(board):
        for (y, isAlive) in enumerate(row):
            if isAlive:
                drawCell(screen, (x,y))

    pygame.display.flip()