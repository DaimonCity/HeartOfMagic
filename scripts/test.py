import pygame
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)

    tiles_dict = {'#': Tile(), '=': WallTile(), '.': FloorTile()}
    map_txt = open('data\\map.txt', 'r').read()
    _map = [list(i) for i in map_txt.split('\n')]
    board = Board(screen=screen, map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.get_click(event.pos)
        board.render(screen)
        pygame.display.update()
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.display.flip()
