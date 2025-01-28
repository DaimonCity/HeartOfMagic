import pygame, pprint
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Entities.PlayerClass import Hero
if __name__ == '__main__':
    FPS = 60
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = width, height = screen.get_size()

    screen.get_width()
    clock = pygame.time.Clock()
    top = 0
    left = 0

    tiles_dict = {'#': Tile(), '=': WallTile(), '.': FloorTile(), ' ': WoidTile()}
    map_txt = open('data\\map.txt', 'r').read()
    map = [list(i) for i in map_txt.split('\n')]
    for row in map:
        if len(row) < max([len(i) for i in map]):
            row += [' '] * (max([len(i) for i in map]) - len(row))
    board = Board(screen=screen, map=map, tiles_dict=tiles_dict, left=10, top=20, cell_size=64)
    zoom = 1
    keys = dict()
    keyboard =(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x)
    for i in keyboard:
        keys[i] = 0
    running = True
    player = Hero(screen)
    spell_group = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keyboard:
                    keys[event.key] = True
                if  event.key == pygame.K_F11:
                    if pygame.display.is_fullscreen():
                        screen = pygame.display.set_mode((width, height))
                    else:
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    size = screen.get_size()
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key in keyboard:
                    keys[event.key] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.cast((left, top), spell_group=spell_group, vec=event.pos)

        if any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]):
            left, top = player.move(((int(keys[pygame.K_d]) - int(keys[pygame.K_a])), (int(keys[pygame.K_s]) - int(keys[pygame.K_w]))), left=left, top=top, screen=screen)
        if keys[pygame.K_c]:
            zoom += 0.1
        if keys[pygame.K_x]:
            if  zoom - 0.1 > 0.1:
                zoom -= 0.1
        board.render(screen)
        player.render(screen)
        board.update(screen, left, top)
        spell_group.update(map_move=(left, top))
        spell_group.draw(screen)

        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
    pygame.display.flip()

