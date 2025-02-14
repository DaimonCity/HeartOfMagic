from classes.Animations.AnimationsClasses import AnimatedSprite
from classes.Entities.EntityClass import HpBar
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import *
from classes.Entities.PlayerClass import Hero
from classes.Entities.EnemyClass import *
from classes.Generation.generation_floor import Map, EMPTY_MAP, choice_cord
import pygame

if True:
    FPS = 60
    frame = 0
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  #
    size = width, height = screen.get_size()
    wizard = AnimatedSprite(load_image("ToDownMag-Sheet.png"), 8, 1, 32 * 8, 32)
    bolt = AnimatedSprite(load_image("Bolt-Sheet.png"), 9, 1, 32 * 8, 32)

    animation_of_magic = {Spell: bolt}
    clock = pygame.time.Clock()
    floor = Map(EMPTY_MAP)
    top = 0
    left = 0
    zoom = 3
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    tiles_dict = {0: FloorTile, 1: WallTile, 2: DoorTile, 3: UpperLeftCornerTile, 4: UpperLeftCornerTile,
                  5: DownerLeftCornerTile, 6: UpperRightCornerTile, 7: DownerRightCornerTile,
                  8: LeftWallTile, 9: TToUpTile, 11: RightWallTile, 12: TToAllTile, 13: TToDownTile,
                  14: TLeftWallTile, 15: TRightWallTile, 16: TLeftWallForRoomTile, 17: SideDoorTile}
    casting = False
    _map = floor.get_map()

    b_mose_pos = screen.get_rect().center
    keys = dict()
    keyboard = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x, pygame.MOUSEBUTTONDOWN)
    for i in keyboard:
        keys[i] = 0

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, cell_size=64)
    Wand_UI = UI(screen=screen, any_map=['000000'], tiles_dict={'0': Vacous}, left=20, top=20, cell_size=32 * 3)
    Inventory_UI = UI(screen=screen, any_map=['00000'], tiles_dict={'0': Bolt}, left=screen.get_width() - 32 * 3 * 5,
                      top=20, cell_size=32 * 3)
    Inventory_UI.board = [[Triple(board), Bolt(board), Unstable(board), Sin(board), Vacous(board), Vacous(board)]]
    inventory_chose = None
    wand_chose = None

    # init_top, init_left = floor.spawn_player_and_exit(board, size)
    board.left, board.top = 10, 10

    player = Hero(screen, wizard, board=board)
    player.spell_line = [i.__class__ for i in Wand_UI.board[0]]
    cooldown_time = time()

    # screen.blit()
    hp_bar = HpBar(load_image('HP-Bar.png'), 202, 1, 128 * 202, 32, player, screen, board)
    spell_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_speel_group = pygame.sprite.Group()
    enemy_group.add([Ranger(spell_group=enemy_speel_group, board=board) for i in range(3)])
    enemy_group.add([Closer(spell_group=enemy_speel_group, board=board) for i in range(3)])

    running = True
    while running:
        frame = frame % 60 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (Inventory_UI.get_click(event.pos) is not None) or (Wand_UI.get_click(event.pos) is not None):
                    inventory_chose = Inventory_UI.get_click(event.pos) if Inventory_UI.get_click(
                        event.pos) is not None else inventory_chose
                    wand_chose = Wand_UI.get_click(event.pos) if Wand_UI.get_click(
                        event.pos) is not None else wand_chose
                    if (inventory_chose is not None) and (wand_chose is not None):
                        Inventory_UI.board[inventory_chose[1]][inventory_chose[0]], Wand_UI.board[wand_chose[1]][
                            wand_chose[0]] = Wand_UI.board[wand_chose[1]][wand_chose[0]], \
                            Inventory_UI.board[inventory_chose[1]][inventory_chose[0]]
                        player.spell_line = [i.__class__ for i in Wand_UI.board[0]]
                        inventory_chose = None
                        wand_chose = None

                else:
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
                if event.key == pygame.K_F11:
                    if pygame.display.is_fullscreen():
                        screen = pygame.display.set_mode((width, height))
                    else:
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    size = screen.get_size()

        if any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]):
            left, top = player.move(normolize_vec(
                ((int(keys[pygame.K_d]) - int(keys[pygame.K_a])), (int(keys[pygame.K_s]) - int(keys[pygame.K_w])))),
                left=left, top=top, screen=screen, mose_pos=mouse_pos)

        if keys[pygame.MOUSEBUTTONDOWN]:
            if time() - cooldown_time >= player.cooldown:
                vec = ((mouse_pos[0] * zoom + mouse_pos[0] * (1 - zoom)) +
                       (player.rect.center[0] - screen.get_rect().center[0]) * (1 - zoom),
                       (mouse_pos[1] * zoom + mouse_pos[1] * (1 - zoom)) +
                       (player.rect.center[1] - screen.get_rect().center[1]) * (1 - zoom))
                player.cast((left, top), spell_group=spell_group, vec=vec, board=board)
                cooldown_time = time()

        board.enemy_group = enemy_group
        board.enemy_spell_group = enemy_speel_group

        left += (b_mose_pos[0] - mouse_pos[0]) / 70
        top += (b_mose_pos[1] - mouse_pos[1]) / 70
        b_mose_pos = (
            b_mose_pos[0] - (b_mose_pos[0] - mouse_pos[0]) / 5, b_mose_pos[1] - (b_mose_pos[1] - mouse_pos[1]) / 5)
        player.update(center=(player.rect.center[0] + (b_mose_pos[0] - mouse_pos[0]) / 70,
                              player.rect.center[1] + (b_mose_pos[1] - mouse_pos[1]) / 70), map_move=(left, top),
                      board=board)

        if keys[pygame.K_c]:
            zoom += 0.05
        if keys[pygame.K_x]:
            if zoom - 0.1 > 0.1:
                zoom -= 0.05
        board.render(screen=screen)
        board.update(left, top)
        wizard.update(any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]))
        player.image = wizard.image
        player.render(screen)

        casting = True if spell_group else False
        bolt.update(casting)
        board.update(left, top)
        spell_group.draw(screen)
        board.player_spell_group = spell_group
        enemy_group.draw(screen)
        enemy_speel_group.draw(screen)
        spell_group.update(map_move=(left, top), anim=bolt.image, board=board)
        enemy_group.update(map_move=(left, top), player=player, board=board)
        enemy_speel_group.update(map_move=(left, top), board=board)

        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (
            width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        Inventory_UI.render()
        Wand_UI.render()
        pygame.display.update()
        hp_bar.update()
        hp_bar.render()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        if player.hp <= 0:
            pass
    pygame.display.flip()
