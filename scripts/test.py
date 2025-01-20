import pygame
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Entities.PlayerClass import Hero

if __name__ == '__main__':
    FPS = 30
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    tiles_dict = {'#': Tile(), '=': WallTile(), '.': FloorTile()}
    map_txt = open('data\\map.txt', 'r').read()
    _map = [list(i) for i in map_txt.split('\n')]
    board = Board(screen=screen, map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=50)

    keys = dict()
    for i in pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d:
        keys[i] = 0
    running = True
    player = Hero()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                    keys[event.key] = True
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                    keys[event.key] = False
        if any(list(keys.values())):
            player.move((int(keys[pygame.K_d]) - int(keys[pygame.K_a]),
                         int(keys[pygame.K_s]) - int(keys[pygame.K_w])))
        board.render(screen)
        player.render(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
    pygame.display.flip()
