import pygame
import pygame.display as display

from game import Game


def main():
    pygame.init()
    display.set_caption("Game of Life")    
    gridSize = 50,40
    game = Game(gridSize, display)

    game.runGameLoop(pygame.event, pygame.time.set_timer)


if __name__ == '__main__': 
    main()        