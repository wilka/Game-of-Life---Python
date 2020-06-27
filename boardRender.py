import pygame.draw as draw
import colors
from point import Point

class BoardRender:
    def __init__(self, surface, board, cellSize):
        self.surface = surface
        self.board = board
        self.cellSize = cellSize
        self.highlightCell = (-1, -1)

    def draw(self):
        for cell in self.board.cells():
            if cell.isAlive:
                self.drawLiveCell(self.surface, cell.position)
            else:
                self.drawDeadCell(self.surface, cell.position)

    def mouseMoveTest(self, mouse_pos):
        self.highlightCell = self.mousePosToCell(mouse_pos)

    def mousePosToCell(self, mouse_pos):
        (x, y) = mouse_pos
        (cellWidth, cellHeight) = self.cellSize
        x /= cellWidth
        y /= cellHeight
        
        return Point(int(x), int(y))

    def clickTest(self, mouse_pos):
        if mouse_pos[0] >= 0 and mouse_pos[1] >= 0:
            clickedCell = self.mousePosToCell(mouse_pos)
            try:
                self.board.setCell(clickedCell, not self.board.isCellAlive(clickedCell))
            except IndexError:
                pass

    def drawLiveCell(self, surface, position):
        (x, y) = position
        (cellWidth, cellHeight) = self.cellSize

        x *= cellWidth
        y *= cellHeight

        mainColor = colors.cellLiveHoverColor if position == self.highlightCell else colors.cellMainColor

        draw.rect(surface, mainColor, ((x, y), self.cellSize))
        draw.line(surface, colors.cellLightEdgeColor, (x,y), (x, y + cellHeight))
        draw.line(surface, colors.cellLightEdgeColor, (x,y), (x + cellWidth, y))
        draw.line(surface, colors.cellDarkEdgeColor, (x, y + cellHeight), (x + cellWidth, y + cellHeight))
        draw.line(surface, colors.cellDarkEdgeColor, (x + cellWidth, y), (x + cellWidth, y + cellHeight))

    def drawDeadCell(self, surface, position):
        if position == self.highlightCell:
            (x, y) = position
            
            (cellWidth, cellHeight) = self.cellSize

            x *= cellWidth
            y *= cellHeight

            draw.rect(surface, colors.cellDeadHoverColor, ((x, y), self.cellSize))
