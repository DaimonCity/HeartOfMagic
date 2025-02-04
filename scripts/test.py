import pygame, pprint
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board  # Импортируем BoardClass
from classes.Entities.PlayerClass import Hero
from classes.Generation.generation_floor import Map, EMPTY_MAP, choice_cord
from classes.Boards.FloarBoard import Board as FloarBoard  # Импортируем FloarBoard

if __name__ == 'main':
    FPS = 60
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  #
    size = width, height = screen.get_size()

    screen.get_width()
    clock = pygame.time.Clock()
    top = 0
    left = 0

    floor = Map(EMPTY_MAP)
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    tiles_dict = {0: FloorTile(), 1: WallTile(), 2: DoorTile(), 3: UpperLeftCornerTile(), 4: UpperLeftCornerTile(),
                  5: DownerLeftCornerTile(), 6: UpperRightCornerTile(), 7: DownerRightCornerTile(),
                  8: LeftWallTile(), 9: TToUpTile(), 11: RightWallTile(), 12: TToAllTile(), 13: TToDownTile(),
                  14: TLeftWallTile(), 15: TRightWallTile(), 16: TLeftWallForRoomTile(), 17: SideDoorTile()}

    _map = floor.get_map()

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=left, top=top, cell_size=64)
    floar_board = FloarBoard(3,3)  # Создаем экземпляр FloarBoard
    floar_board.set_view(left, top, 200)
    zoom = 1
    keys = dict()
    keyboard = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x)
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
                if event.key == pygame.K_F11:
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
                floar_board.get_click(event.pos) # Обрабатываем клик FloarBoard

        if any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]):
            move_vector = ((int(keys[pygame.K_d]) - int(keys[pygame.K_a])), (int(keys[pygame.K_s]) - int(keys[pygame.K_w])))
            left, top = player.move(move_vector, left=left, top=top, screen=screen, board=board)
        if keys[pygame.K_c]:
            zoom += 0.1
        if keys[pygame.K_x]:
            if zoom - 0.1 > 0.1:
                zoom -= 0.1

        screen.fill((0, 0, 0))
        board.render()
        floar_board.render(screen)
        player.render(screen)
        board.update(left, top)
        spell_group.update(map_move=(left, top))
        spell_group.draw(screen)

        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (
            width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.flip()