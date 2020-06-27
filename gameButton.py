from pygame import Rect

class GameButton:
    DEFAULT_COLOR = (200, 0, 0)
    HOVER_COLOR = (100, 0, 0)

    def __init__(self, action):
        self.action = action
        self.size = (45, 25)
        self.color = self.DEFAULT_COLOR
        self.displayRect = Rect(0, 0, 0, 0)

    def setDisplayRect(self, displayRect):
        self.displayRect = Rect(displayRect)

    def clickTest(self, mouseDownPos):
        if self.displayRect.collidepoint(mouseDownPos):
            self.action()

    def mouseMoveTest(self, mousePos):
        if self.displayRect.collidepoint(mousePos):
            self.color = self.HOVER_COLOR
        else:
            self.color = self.DEFAULT_COLOR