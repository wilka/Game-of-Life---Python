from pygame import Rect, draw
import pygame 

class GameButton:
    def __init__(self, action, text):
        self.action = action
        self.size = (85, 35)
        self.fillColor = (0, 180, 0)
        self.outlineColor = (0, 110, 0)
        self.displayRect = Rect(0, 0, 0, 0)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 22)
        self.isSet = False
        self.isHover = False

    def adjustColorForHover(self, color):
        (r, g, b) = color
        return (r, g + 60, b)

    def adjustColorForSet(self, color):
        (r, g, b) = color
        return (r + 200, g - 100, b)        

    def clickTest(self, mouseDownPos):
        if self.displayRect.collidepoint(mouseDownPos):
            if self.action():
                self.isSet = True
            else:
                self.isSet = False

    def mouseMoveTest(self, mousePos):
        if self.displayRect.collidepoint(mousePos):
            self.isHover = True
        else:
            self.isHover = False

    def transformColor(self, color):
        if self.isHover:
            color = self.adjustColorForHover(color)
        if self.isSet:
            color = self.adjustColorForSet(color)            

        return color

    def draw(self, surface, topLeft):
        (x, y) = topLeft
        self.displayRect = Rect((x, y, self.size[0], self.size[1]))
        
        draw.rect(surface, self.transformColor(self.fillColor), self.displayRect)
        draw.rect(surface, self.transformColor(self.outlineColor), self.displayRect, 4)

        # Draw a bit of text on teh button
        
        textSize = self.font.size(self.text)
        textsurface = self.font.render(self.text, True, (0, 0, 0))

        textX = topLeft[0] + self.size[0] / 2 - textSize[0] / 2
        textY = topLeft[1] + self.size[1] / 2 - textSize[1] / 2

        surface.blit(textsurface, (textX, textY))