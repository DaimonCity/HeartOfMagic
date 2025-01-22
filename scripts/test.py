import pygame, pprint
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Entities.PlayerClass import Hero
if __name__ == '__main__':
    FPS = 30
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    screen.get_width()
    clock = pygame.time.Clock()
    top = 0
    left = 0

    tiles_dict = {'#': Tile(), '=': WallTile(), '.': FloorTile()}
    map_txt = open('data\\map.txt', 'r').read()
    _map = [list(i) for i in map_txt.split('\n')]
    board = Board(screen=screen, map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=64)
    zoom = 1
    keys = dict()
    keyboard =(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x)
    for i in keyboard:
        keys[i] = 0
    running = True
    player = Hero(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keyboard:
                    keys[event.key] = True
            if event.type == pygame.KEYUP:
                if event.key in keyboard:
                    keys[event.key] = False
        if any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]):
            left, top = player.move(((int(keys[pygame.K_d]) - int(keys[pygame.K_a])) * zoom, (int(keys[pygame.K_s]) - int(keys[pygame.K_w])) * zoom), left=left, top=top, screen=screen)

        if keys[pygame.K_c]:
            zoom += 0.1
        if keys[pygame.K_x]:
            if zoom - 0.1 > 0.1:
                zoom -= 0.1
        board.render(screen)
        player.render(screen)
        board.update(screen, left, top, zoom)
        player.update(zoom=zoom)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
    pygame.display.flip()

