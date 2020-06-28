from boardRender import BoardRender
from buttonBar import ButtonBar
from gameBoard import GameBoard
from gameButton import GameButton
from point import Point
from time import sleep
import colors
import pygame
import gameBoardReaderWriter

class Game:
    def __init__(self, grid_size, display):
        self.grid_size = grid_size
        self.board = self._make_default_board()
        self.button_area_height = 100
        self.cell_size = 25,25
        self.screen_size = width, height = self.grid_size[0] * self.cell_size[0], (self.grid_size[1] * self.cell_size[1]) + self.button_area_height
        self.screen = display.set_mode(self.screen_size)
        self.display = display

        buttons = [GameButton(self._toggle_pause, "Pause"), 
                    GameButton(self._reset_game, "Reset"), 
                    GameButton(self._clear_game, "Clear"),
                    GameButton(self._load_board, "Load"),
                    GameButton(self._save_board, "Save"),
                    ]

        self.button_bar = ButtonBar(self.screen_size, self.button_area_height, buttons)
        self.is_paused = False


    def _make_default_board(self):
        board = GameBoard(self.grid_size)

        # Glider at the top left
        board.set_cell(Point(1, 0), True)
        board.set_cell(Point(2, 1), True)
        board.set_cell(Point(0, 2), True)
        board.set_cell(Point(1, 2), True)
        board.set_cell(Point(2, 2), True)

        # Blinker at the top middle
        board.set_cell(Point(20, 2), True)
        board.set_cell(Point(20, 3), True)
        board.set_cell(Point(20, 4), True)        

        return board

    def _load_board(self):
        new_board = gameBoardReaderWriter.read_board()
        if new_board:
            self.board = new_board

    def _save_board(self):
        gameBoardReaderWriter.write_board(self.board)
        
    def _toggle_pause(self):
        self.is_paused = not self.is_paused
        return self.is_paused


    def _reset_game(self):
        self.board = self._make_default_board()


    def _clear_game(self):
        self.board = GameBoard(self.grid_size)


    def run_game_loop(self, getGameEvent, setEventTimer):
        
        mouse_move_pos = (0, 0)
        
        MOVE_TO_NEXT_GENERATION = pygame.USEREVENT + 1
        setEventTimer(MOVE_TO_NEXT_GENERATION, 225)

        while True:
            mouse_down_pos = (-1, -1)
            for event in getGameEvent.get():
                if event.type == pygame.QUIT: 
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down_pos = event.pos
                if event.type == pygame.MOUSEMOTION:
                    mouse_move_pos = event.pos
                if event.type == MOVE_TO_NEXT_GENERATION:
                    if not self.is_paused:
                        self.board = self.board.next_generation()

            self.screen.fill(colors.GAME_BACKGROUND)

            board_render = BoardRender(self.screen, self.board, self.cell_size)
            board_render.mouse_move_test(mouse_move_pos)
            board_render.click_test(mouse_down_pos)
            board_render.draw()

            self.button_bar.mouse_move_test(mouse_move_pos)
            self.button_bar.click_test(mouse_down_pos)
            self.button_bar.draw(self.screen)
            
            self.display.flip()

            pygame.time.wait(20)
