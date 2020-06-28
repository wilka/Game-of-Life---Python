from pygame import Rect, draw
import pygame 

class GameButton:
    def __init__(self, action, text):
        self.action = action
        self.size = (85, 35)
        self.fill_color = (0, 180, 0)
        self.outline_color = (0, 110, 0)
        self.display_rect = Rect(0, 0, 0, 0)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 22)
        self.isSet = False
        self.isHover = False

    def _adjust_color_for_hover(self, color):
        (r, g, b) = color
        return (r, g + 60, b)

    def _adjust_color_for_set(self, color):
        (r, g, b) = color
        return (r + 200, g - 100, b)        

    def click_test(self, mouseDownPos):
        if self.display_rect.collidepoint(mouseDownPos):
            if self.action():
                self.isSet = True
            else:
                self.isSet = False

    def mouse_move_test(self, mousePos):
        if self.display_rect.collidepoint(mousePos):
            self.isHover = True
        else:
            self.isHover = False

    def _transform_color(self, color):
        if self.isHover:
            color = self._adjust_color_for_hover(color)
        if self.isSet:
            color = self._adjust_color_for_set(color)            

        return color

    def draw(self, surface, topLeft):
        (x, y) = topLeft
        self.display_rect = Rect((x, y, self.size[0], self.size[1]))
        
        # Draw button rect
        draw.rect(surface, self._transform_color(self.fill_color), self.display_rect)
        draw.rect(surface, self._transform_color(self.outline_color), self.display_rect, 4)

        # Draw text on the button
        textSize = self.font.size(self.text)
        textsurface = self.font.render(self.text, True, (0, 0, 0))

        textX = topLeft[0] + self.size[0] / 2 - textSize[0] / 2
        textY = topLeft[1] + self.size[1] / 2 - textSize[1] / 2

        surface.blit(textsurface, (textX, textY))