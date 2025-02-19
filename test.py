from pprint import pprint

from classes.Animations.AnimationsClasses import AnimatedSprite
from classes.Entities.EntityClass import HpBar
from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import *
from classes.Entities.PlayerClass import Hero
from classes.Entities.EnemyClass import *
from classes.Generation.generation_floor import Map, choice_cord
import pygame

FPS = 60


def start_params():
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  #
    width, height = screen.get_size()
    tiles_dict = {0: FloorTile, 1: WallTile, 2: DoorTile, 3: UpperLeftCornerTile, 4: UpperLeftCornerTile,
                  5: DownerLeftCornerTile, 6: UpperRightCornerTile, 7: DownerRightCornerTile,
                  8: LeftWallTile, 9: TToUpTile, 11: RightWallTile, 12: TToAllTile, 13: TToDownTile,
                  14: TLeftWallTile, 15: TRightWallTile, 16: TLeftWallForRoomTile, 17: SideDoorTile, 20: Exit}

    frame = 0
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    wizard = AnimatedSprite(load_image("ToDownMag-Sheet.png"), 8, 1, 32 * 8, 32)
    bolt = AnimatedSprite(load_image("Bolt-Sheet.png"), 9, 1, 32 * 8, 32)
    clock = pygame.time.Clock()
    keys = dict()
    keyboard = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x, pygame.MOUSEBUTTONDOWN)
    for i in keyboard:
        keys[i] = 0
    wand_ui = UI(screen=screen, any_map=['000000'], tiles_dict={'0': Vacous}, left=20, top=20, cell_size=32 * 3)
    inventory_ui = UI(screen=screen, any_map=['00000'], tiles_dict={'0': Bolt}, left=screen.get_width() - 32 * 3 * 5,
                      top=20, cell_size=32 * 3)
    player = Hero(screen, wizard)
    return screen, width, height, tiles_dict, frame, wizard, bolt, clock, wand_ui, inventory_ui, keyboard, keys, player


def test(screen, width, height, tiles_dict, frame, wizard, bolt, clock, wand_ui, inventory_ui, keyboard, keys, player,
         empty_map):
    inventory_chose = None
    wand_chose = None
    next_floor = False
    b_mose_pos = screen.get_rect().center
    top = height / 2
    left = width / 2
    zoom = 3

    floor = Map(empty_map)
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    c_left, c_top = floor.add_exit()
    _map = floor.get_map()

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, cell_size=64)
    player.board = board
    inventory_ui.board = [[Triple(board), Bolt(board), Unstable(board), Sin(board), Vacous(board), Vacous(board)]]

    left, top = left - board.cell_size * c_top, top - board.cell_size * c_left
    print(left, top)

    player.spell_line = [i.__class__ for i in wand_ui.board[0]]

    hp_bar = HpBar(load_image('HP-Bar-Sheet.png'), 202, 1, 256 * 202, 32, player, screen)
    spell_group = pygame.sprite.Group()

    cooldown_time = time()
    enemy_group = pygame.sprite.Group()
    enemy_spell_group = pygame.sprite.Group()
    enemy_group.add([Ranger(spell_group=enemy_spell_group, board=board) for _ in range(20)])
    enemy_group.add([Closer(spell_group=enemy_spell_group, board=board) for _ in range(5)])
    mouse_pos = (0, 0)
    running = True
    while running:
        frame = frame % 60 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (inventory_ui.get_click(event.pos) is not None) or (wand_ui.get_click(event.pos) is not None):
                    inventory_chose = inventory_ui.get_click(event.pos) if inventory_ui.get_click(
                        event.pos) is not None else inventory_chose
                    wand_chose = wand_ui.get_click(event.pos) if wand_ui.get_click(
                        event.pos) is not None else wand_chose
                    if (inventory_chose is not None) and (wand_chose is not None):
                        inventory_ui.board[inventory_chose[1]][inventory_chose[0]], wand_ui.board[wand_chose[1]][
                            wand_chose[0]] = wand_ui.board[wand_chose[1]][wand_chose[0]], \
                            inventory_ui.board[inventory_chose[1]][inventory_chose[0]]
                        player.spell_line = [i.__class__ for i in wand_ui.board[0]]
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
                        screen = pygame.display.set_mode((width, width), pygame.FULLSCREEN)
                    width, height = screen.get_size()

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

        if pygame.sprite.spritecollideany(player, board.exit_group):
            next_floor = True
            running = False

        board.enemy_group = enemy_group
        board.enemy_spell_group = enemy_spell_group

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
        board.update(left, top)
        board.render(screen=screen)
        wizard.update(any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]))
        player.image = wizard.image
        player.render(screen)

        casting = True if spell_group else False
        bolt.update(casting)
        board.update(left, top)
        spell_group.draw(screen)
        board.player_spell_group = spell_group
        enemy_group.draw(screen)
        enemy_spell_group.draw(screen)
        spell_group.update(map_move=(left, top), anim=bolt.image, board=board)
        enemy_group.update(map_move=(left, top), player=player, board=board)
        enemy_spell_group.update(map_move=(left, top), board=board)

        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (
            width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        hp_bar.update()
        inventory_ui.render()
        wand_ui.render()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        if player.hp <= 0:
            exit()
    pygame.display.flip()
    if next_floor is True:
        return True
    return False
