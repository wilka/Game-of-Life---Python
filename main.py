import pygame
import pygame.display as display

from game import Game


def main():
    pygame.init()
    display.set_caption("Game of Life")    
    grid_size = (50,40)
    game = Game(grid_size, display)

    game.run_game_loop(pygame.event, pygame.time.set_timer)


if __name__ == '__main__': 
    main()        