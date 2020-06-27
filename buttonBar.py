import colors
import pygame.draw as draw

class ButtonBar:
    def __init__(self, screenSize, buttonAreaHeight, button):
        self.screenSize = screenSize
        self.button = button
        self.buttonAreaHeight = buttonAreaHeight

    def draw(self, surface):
        (width, height) = self.screenSize
        
        buttonArea = (0, height - self.buttonAreaHeight, width, self.buttonAreaHeight)
        (x, y, width, height) = buttonArea

        # Draw button bar
        draw.rect(surface, colors.buttonAreaColor, buttonArea)

        # draw the buttons
        buttonSize = self.button.size

        buttonDisplayRect = ((x + width / 2) - buttonSize[0], (y + height / 2) - buttonSize[1] / 2, buttonSize[0], buttonSize[1])
        self.button.setDisplayRect(buttonDisplayRect)

        draw.rect(surface, self.button.color, buttonDisplayRect)

