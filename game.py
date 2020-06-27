from boardRender import BoardRender
from buttonBar import ButtonBar
from gameBoard import GameBoard
from gameButton import GameButton
from point import Point
from time import sleep
import colors
import pygame

class Game:
    def __init__(self, gridSize, display):
        self.gridSize = gridSize
        self.board = self.makeDefaultBoard()
        self.buttonAreaHeight = 100
        self.cellSize = 25,25
        self.screenSize = width, height = self.gridSize[0] * self.cellSize[0], (self.gridSize[1] * self.cellSize[1]) + self.buttonAreaHeight
        self.screen = display.set_mode(self.screenSize)
        self.display = display

        self.pauseButton = GameButton(self.togglePause)
        self.buttonBar = ButtonBar(self.screenSize, self.buttonAreaHeight, self.pauseButton)
        self.isPaused = False


    def makeDefaultBoard(self):
        board = GameBoard(self.gridSize)

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

        return board


    def togglePause(self):
        self.isPaused = not self.isPaused


    def runGameLoop(self, gameEvent):
        mouse_pos = (0, 0)

        while True:
            for event in gameEvent.get():
                if event.type == pygame.QUIT: 
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

            self.screen.fill(colors.gameBackground)

            boardRender = BoardRender(self.cellSize)
            boardRender.draw(self.screen, self.board)

            self.buttonBar.draw(self.screen)
            self.pauseButton.clickTest(mouse_pos)
            
            mouse_pos = (0, 0)
            self.display.flip()

            if not self.isPaused:
                self.board = self.board.nextGeneration()

            sleep(0.25)
