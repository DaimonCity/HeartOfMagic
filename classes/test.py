import pygame
from classes.Board import Board

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)
    board = Board(100, 100)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.display.flip()
