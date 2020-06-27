from pygame import Rect

class GameButton:
    def __init__(self, action):
        self.action = action
        self.size = (45, 25)
        self.color = (200, 0, 0)

    def setDisplayRect(self, displayRect):
        self.displayRect = Rect(displayRect)

    def clickTest(self, mouseDownPos):
        if self.displayRect.collidepoint(mouseDownPos):
            self.action()