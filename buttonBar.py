import colors
import pygame.draw as draw

class ButtonBar:
    def __init__(self, screenSize, buttonAreaHeight, buttons):
        self.screenSize = screenSize
        self.buttons = buttons
        self.buttonAreaHeight = buttonAreaHeight

    def draw(self, surface):
        (width, height) = self.screenSize
        
        buttonArea = (0, height - self.buttonAreaHeight, width, self.buttonAreaHeight)
        (x, y, width, height) = buttonArea

        # Draw button bar
        draw.rect(surface, colors.buttonAreaColor, buttonArea)

        buttonSpace = 10

        # draw the buttons
        totalButtonWidth = sum(map(lambda b: b.size[0], self.buttons)) + buttonSpace * (len(self.buttons) - 1)
        maxButtonHeight = max(map(lambda b: b.size[1], self.buttons))

        drawStartPositionX = (x + width / 2) - totalButtonWidth / 2
        drawStartPositionY = (y + height / 2) - maxButtonHeight / 2

        for button in self.buttons:
            button.draw(surface, (drawStartPositionX, drawStartPositionY))
            drawStartPositionX = drawStartPositionX + button.size[0] + buttonSpace

    def clickTest(self, mouse_pos):
        for button in self.buttons:
            button.clickTest(mouse_pos)

    def mouseMoveTest(self, mouse_pos):
        for button in self.buttons:
            button.mouseMoveTest(mouse_pos)

