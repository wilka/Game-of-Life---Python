import sys
from time import sleep
import pygame
import pygame.display as display
import pygame.draw as draw
from gameBoard import GameBoard
from point import Point

pygame.init()

cellSize = 25,25
gridSize = 50,40


black = 0, 0, 0

buttonAreaHeight = 100

display.set_caption("Game of Life")
screenSize = width, height = gridSize[0] * cellSize[0], (gridSize[1] * cellSize[1]) + buttonAreaHeight
screen = display.set_mode(screenSize)

buttonArea = (0, height - buttonAreaHeight, width, buttonAreaHeight)
buttonAreaColor = 255, 255, 255

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

def drawButtons(surface, button):
    draw.rect(surface, buttonAreaColor, buttonArea)

    (x, y, width, height) = buttonArea

    buttonSize = button.size

    playPauseButtonRect = ((x + width / 2) - buttonSize[0], (y + height / 2) - buttonSize[1] / 2, buttonSize[0], buttonSize[1])
    button.setDisplayRect(playPauseButtonRect)

    draw.rect(surface, button.color, playPauseButtonRect)

class GameButton:
    def __init__(self, action):
        self.action = action
        self.size = (45, 25)
        self.color = (200, 0, 0)

    def setDisplayRect(self, displayRect):
        self.displayRect = pygame.Rect(displayRect)

    def clickTest(self, mouseDownPos):
        if self.displayRect.collidepoint(mouseDownPos):
            self.action()

isPaused = False

def togglePause(): 
    global isPaused
    isPaused = not isPaused

def main():
    board = GameBoard(gridSize)

    # Glider at the top left
    board.setCell(Point(1, 0), True)
    board.setCell(Point(2, 1), True)
    board.setCell(Point(0, 2), True)
    board.setCell(Point(1, 2), True)
    board.setCell(Point(2, 2), True)

    # Blinker at the top middle
    board.setCell(Point(20, 2), True)
    board.setCell(Point(20, 3), True)
    board.setCell(Point(20, 4), True)

    mouse_pos = (0,0)
    
    pauseButton = GameButton(togglePause)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

        screen.fill(black)

        for cell in board.cells():
            if cell.isAlive:
                drawCell(screen, cell.position)

        drawButtons(screen, pauseButton)
        pauseButton.clickTest(mouse_pos)
        
        mouse_pos = (0, 0)
        pygame.display.flip()

        if not isPaused:
            board = board.nextGeneration()

        sleep(0.25)

if __name__ == '__main__': 
    main()        