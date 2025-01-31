import pygame, pprint
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Entities.PlayerClass import Hero
from classes.Entities.EnemyClass import *
from classes.Generation.generation_floor import Map, EMPTY_MAP, choice_cord

if __name__ == '__main__':
    FPS = 60
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #
    size = width, height = screen.get_size()

    screen.get_width()
    clock = pygame.time.Clock()
    top = 0
    left = 0
    zoom = 1
    floor = Map(EMPTY_MAP)
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    tiles_dict = {0: FloorTile(), 1: WallTile(), 2: DoorTile(), 3: UpperLeftCornerTile(), 4: UpperLeftCornerTile(),
                  5: DownerLeftCornerTile(), 6: UpperRightCornerTile(), 7: DownerRightCornerTile(),
                  8: LeftWallTile(), 9: TToUpTile(), 11: RightWallTile(), 12: TToAllTile(), 13: TToDownTile(),
                  14: TLeftWallTile(), 15: TRightWallTile(), 16: TLeftWallForRoomTile(), 17: SideDoorTile()}

    _map = floor.get_map()


    # tiles_dict = {'#': Tile(), '=': WallTile(), '.': FloorTile(), ' ': WoidTile()}
    # map_txt = open('data\\map.txt', 'r').read()
    # map = [list(i) for i in map_txt.split('\n')]
    #
    #
    # for row in map:
    #     if len(row) < max([len(i) for i in map]):
    #         row += [' '] * (max([len(i) for i in map]) - len(row))



    keys = dict()
    keyboard =(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x, pygame.MOUSEBUTTONDOWN)
    for i in keyboard:
        keys[i] = 0

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=64)
    player = Hero(screen)
    cooldown_time = time()

    spell_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_speel_group = pygame.sprite.Group()
    enemy_group.add([Ranger(spell_group=enemy_speel_group) for i in range(3)])
    enemy_group.add([Closer(spell_group=enemy_speel_group) for i in range(3)])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                keys[pygame.MOUSEBUTTONDOWN] = True
            if event.type == pygame.MOUSEBUTTONUP:
                keys[pygame.MOUSEBUTTONDOWN] = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.KEYUP:
                if event.key in keyboard:
                    keys[event.key] = False
            if event.type == pygame.KEYDOWN:
                if event.key in keyboard:
                    keys[event.key] = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                if  event.key == pygame.K_F11:
                    if pygame.display.is_fullscreen():
                        screen = pygame.display.set_mode((width, height))
                    else:
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    size = screen.get_size()


        if any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]):
            left, top = player.move(normolize_vec(((int(keys[pygame.K_d]) - int(keys[pygame.K_a])), (int(keys[pygame.K_s]) - int(keys[pygame.K_w])))), left=left, top=top, screen=screen)
        if keys[pygame.MOUSEBUTTONDOWN]:
            if time() - cooldown_time >= player.cooldown:
                vec = ((mouse_pos[0] * zoom + mouse_pos[0] * (1 - zoom)) +
                       (player.rect.center[0] - screen.get_rect().center[0]) * (1 - zoom),
                       (mouse_pos[1] * zoom + mouse_pos[1] * (1 - zoom)) +
                       (player.rect.center[1] - screen.get_rect().center[1]) * (1 - zoom))
                player.cast((left, top), spell_group=spell_group, vec=vec)
                cooldown_time = time()
        if keys[pygame.K_c]:
            zoom += 0.05
        if keys[pygame.K_x]:
            if  zoom - 0.1 > 0.1:
                zoom -= 0.05
        board.render()
        player.render(screen)
        board.update(left, top)
        spell_group.update(map_move=(left, top))
        spell_group.draw(screen)
        enemy_group.update(map_move=(left, top), player=player)
        enemy_group.draw(screen)
        enemy_speel_group.update(map_move=(left, top))
        enemy_speel_group.draw(screen)


        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
    pygame.display.flip()

