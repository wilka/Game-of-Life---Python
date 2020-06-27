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

        self.buttonBar = ButtonBar(self.screenSize, self.buttonAreaHeight, [GameButton(self.togglePause), GameButton(self.resetGame)])
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

    def resetGame(self):
        self.board = self.makeDefaultBoard()


    def runGameLoop(self, getGameEvent, setEventTimer):
        mouse_pos = (0, 0)
        mouse_move_pos = (0, 0)
        boardRender = BoardRender(self.cellSize)

        MOVE_TO_NEXT_GENERATION = pygame.USEREVENT + 1

        setEventTimer(MOVE_TO_NEXT_GENERATION, 225)


        while True:
            for event in getGameEvent.get():
                if event.type == pygame.QUIT: 
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                if event.type == pygame.MOUSEMOTION:
                    mouse_move_pos = event.pos
                if event.type == MOVE_TO_NEXT_GENERATION:
                    if not self.isPaused:
                        self.board = self.board.nextGeneration()

            self.screen.fill(colors.gameBackground)

            boardRender.draw(self.screen, self.board)

            self.buttonBar.mouseMoveTest(mouse_move_pos)
            self.buttonBar.clickTest(mouse_pos)
            self.buttonBar.draw(self.screen)
            
            mouse_pos = (0, 0)
            self.display.flip()

            pygame.time.wait(20)
