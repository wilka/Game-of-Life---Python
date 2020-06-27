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

        # draw the buttons
        totalButtonWidth = sum(map(lambda b: b.size[0], self.buttons))
        maxButtonHeight = max(map(lambda b: b.size[1], self.buttons))


        drawStartPositionX = (x + width / 2) - totalButtonWidth
        drawStartPositionY = (y + height / 2) - maxButtonHeight / 2

        for button in self.buttons:
            buttonDisplayRect = (drawStartPositionX, drawStartPositionY, button.size[0], button.size[1])
            button.setDisplayRect(buttonDisplayRect)

            draw.rect(surface, button.color, buttonDisplayRect)

            drawStartPositionX = drawStartPositionX + button.size[0]


    def clickTest(self, mouse_pos):
        for button in self.buttons:
            button.clickTest(mouse_pos)

    def mouseMoveTest(self, mouse_pos):
        for button in self.buttons:
            button.mouseMoveTest(mouse_pos)

