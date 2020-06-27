import pygame.draw as draw
import colors

class BoardRender:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def draw(self, surface, board):
        for cell in board.cells():
            if cell.isAlive:
                self.drawCell(surface, cell.position)

    def drawCell(self, surface, position):
        (x, y) = position
        (cellWidth, cellHeight) = self.cellSize

        x *= cellWidth
        y *= cellHeight

        draw.rect(surface, colors.cellMainColor, ((x, y), self.cellSize))
        draw.line(surface, colors.cellLightEdgeColor, (x,y), (x, y + cellHeight))
        draw.line(surface, colors.cellLightEdgeColor, (x,y), (x + cellWidth, y))
        draw.line(surface, colors.cellDarkEdgeColor, (x, y + cellHeight), (x + cellWidth, y + cellHeight))
        draw.line(surface, colors.cellDarkEdgeColor, (x + cellWidth, y), (x + cellWidth, y + cellHeight))

