import sys
from time import sleep
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


def makeNewBoard():
    newBoard = []
    for x in range(gridSize[0]):
        row = []
        for y in range(gridSize[1]):
            row.append(False)
        
        newBoard.append(row)

    return newBoard


board = makeNewBoard()

# Glider at the top left
board[1][0] = True
board[2][1] = True
board[0][2] = True
board[1][2] = True
board[2][2] = True

# Blinker at the top middle
board[20][2] = True
board[20][3] = True
board[20][4] = True


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


def isCellAlive(position, oldboard):
    (x, y) = position
    if x < 0 or y < 0:
        return False

    if x >= len(oldboard) or y >= len(oldboard[0]):
        return False

    return oldboard[x][y]

def numLivingAdjacentCells(position, oldboard):
    (x, y) = position
    count = 0
    if isCellAlive((x-1, y-1), oldboard):
        count+=1
    if isCellAlive((x, y-1), oldboard):
        count+=1
    if isCellAlive((x+1, y-1), oldboard):
        count+=1

    if isCellAlive((x-1, y), oldboard):
        count+=1
    if isCellAlive((x+1, y), oldboard):
        count+=1

    if isCellAlive((x-1, y+1), oldboard):
        count+=1
    if isCellAlive((x, y+1), oldboard):
        count+=1
    if isCellAlive((x+1, y+1), oldboard):
        count+=1            

    return count

def shouldBeAliveInNextGen(position, oldboard):
    (x, y) = position
    livingAdjacents = numLivingAdjacentCells(position, oldboard)
    if oldboard[x][y]:
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        if livingAdjacents < 2:
            return False
        # Any live cell with two or three live neighbours lives on to the next generation.
        if livingAdjacents == 2 or livingAdjacents == 3:
            return True
        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        return False
    else:
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        if livingAdjacents == 3:
            return True
        else:
            return False

    

def nextGeneration(oldBoard):
    newBoard = makeNewBoard()
    for x in range(len(newBoard)):
        for y in range(len(newBoard[x])):
            newBoard[x][y] = shouldBeAliveInNextGen((x, y), oldBoard)
        
    return newBoard

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    for (x, row) in enumerate(board):
        for (y, isAlive) in enumerate(row):
            if isAlive:
                drawCell(screen, (x,y))

    pygame.display.flip()

    board = nextGeneration(board)

    sleep(0.25)