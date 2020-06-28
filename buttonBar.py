import colors
import pygame.draw as draw

class ButtonBar:
    def __init__(self, screen_size, button_area_height, buttons):
        self.screen_size = screen_size
        self.buttons = buttons
        self.button_area_height = button_area_height

    def draw(self, surface):
        (width, height) = self.screen_size
        
        button_area = (0, height - self.button_area_height, width, self.button_area_height)
        (x, y, width, height) = button_area

        # Draw button bar
        draw.rect(surface, colors.BUTTON_AREA_COLOR, button_area)

        buttonSpace = 10

        # draw the buttons
        total_button_width = sum(map(lambda b: b.size[0], self.buttons)) + buttonSpace * (len(self.buttons) - 1)
        max_button_height = max(map(lambda b: b.size[1], self.buttons))

        draw_start_position_x = (x + width / 2) - total_button_width / 2
        draw_start_position_y = (y + height / 2) - max_button_height / 2

        for button in self.buttons:
            button.draw(surface, (draw_start_position_x, draw_start_position_y))
            draw_start_position_x = draw_start_position_x + button.size[0] + buttonSpace

    def click_test(self, mouse_pos):
        for button in self.buttons:
            button.click_test(mouse_pos)

    def mouse_move_test(self, mouse_pos):
        for button in self.buttons:
            button.mouse_move_test(mouse_pos)

