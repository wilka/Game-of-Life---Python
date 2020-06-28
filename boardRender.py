import pygame.draw as draw
import colors
from point import Point

class BoardRender:
    def __init__(self, surface, board, cell_size):
        self.surface = surface
        self.board = board
        self.cell_size = cell_size
        self.highlight_cell = (-1, -1)

    def draw(self):
        for cell in self.board.cells():
            if cell.is_alive:
                self._draw_live_cell(self.surface, cell.position)
            else:
                self._draw_dead_cell(self.surface, cell.position)

    def mouse_move_test(self, mouse_pos):
        self.highlight_cell = self.mouse_pos_to_cell_location(mouse_pos)

    def mouse_pos_to_cell_location(self, mouse_pos):
        (x, y) = mouse_pos
        (cell_width, cell_height) = self.cell_size
        x /= cell_width
        y /= cell_height
        
        return Point(int(x), int(y))

    def click_test(self, mouse_pos):
        if mouse_pos[0] >= 0 and mouse_pos[1] >= 0:
            clicked_cell = self.mouse_pos_to_cell_location(mouse_pos)
            try:
                self.board.set_cell(clicked_cell, not self.board.is_cell_alive(clicked_cell))
            except IndexError:
                pass

    def _draw_live_cell(self, surface, position):
        (x, y) = position
        (cell_width, cell_height) = self.cell_size

        x *= cell_width
        y *= cell_height

        mainColor = colors.CELL_LIVE_HOVER_COLOR if position == self.highlight_cell else colors.CELL_MAIN_COLOR

        draw.rect(surface, mainColor, ((x, y), self.cell_size))
        draw.line(surface, colors.CELL_LIGHT_EDGE_COLOR, (x,y), (x, y + cell_height))
        draw.line(surface, colors.CELL_LIGHT_EDGE_COLOR, (x,y), (x + cell_width, y))
        draw.line(surface, colors.CELL_DARK_EDGE_COLOR, (x, y + cell_height), (x + cell_width, y + cell_height))
        draw.line(surface, colors.CELL_DARK_EDGE_COLOR, (x + cell_width, y), (x + cell_width, y + cell_height))

    def _draw_dead_cell(self, surface, position):
        if position == self.highlight_cell:
            (x, y) = position
            
            (cell_width, cell_height) = self.cell_size

            x *= cell_width
            y *= cell_height

            draw.rect(surface, colors.CELL_DEAD_HOVER_COLOR, ((x, y), self.cell_size))
