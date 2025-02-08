import pygame.sprite

from classes.Animations.AnimationsClasses import AnimatedSprite
from classes.Boards.BoardClass import UI, Board
from classes.Entities.EnemyClass import Ranger, Closer
from classes.Entities.PlayerClass import Hero
from classes.Entities.SpellClass import *
from classes.Generation.generation_floor import Map, choice_cord, EMPTY_MAP
from classes.Tiles.TileClasses import *

FPS = 60


def start_game():
    frame = 0

    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  #
    size = width, height = screen.get_size()
    wizard = AnimatedSprite(load_image("ToDownMag-Sheet.png"), 8, 1, 32 * 8, 32)
    bolt = AnimatedSprite(load_image("Bolt-Sheet.png"), 9, 1, 32 * 8, 32)
    screen.get_width()

    animation_of_magic = {Spell: bolt}
    clock = pygame.time.Clock()
    floor = Map(EMPTY_MAP)
    zoom = 3
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    spawn = floor.add_exit()
    tiles_dict = {0: FloorTile(), 1: WallTile(), 2: DoorTile(), 3: UpperLeftCornerTile(), 4: UpperLeftCornerTile(),
                  5: DownerLeftCornerTile(), 6: UpperRightCornerTile(), 7: DownerRightCornerTile(),
                  8: LeftWallTile(), 9: TToUpTile(), 11: RightWallTile(), 12: TToAllTile(), 13: TToDownTile(),
                  14: TLeftWallTile(), 15: TRightWallTile(), 16: TLeftWallForRoomTile(), 17: SideDoorTile(), 20: Void()}
    casting = False
    _map = floor.get_map()

    top, left = spawn

    # top = -400; left = 450
    # top = 350; left = -250

    b_mose_pos = screen.get_rect().center
    keys = dict()
    keyboard = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x, pygame.MOUSEBUTTONDOWN)
    for i in keyboard:
        keys[i] = 0
    wand_ui = UI(screen=screen, any_map=['0000'], tiles_dict={'0': Vacous()}, left=10, top=0, cell_size=32 * 3)
    inventory_ui = UI(screen=screen, any_map=['00000'], tiles_dict={'0': Bolt()}, left=screen.get_width() - 32 * 3 * 5,
                      top=0, cell_size=32 * 3)
    print(inventory_ui.board)
    inventory_ui.board = [[Triple(), Bolt(), Unstable(), Sin(), Vacous(), Vacous()]]
    inventory_chose = None
    wand_chose = None

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=64)

    player = Hero(screen, wizard)

    player.spell_line = [i.__class__ for i in wand_ui.board[0]]
    cooldown_time = time()

    running = True
    spell_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_spell_group = pygame.sprite.Group()
    enemy_group.add([Ranger(spell_group=enemy_spell_group) for i in range(3)])
    enemy_group.add([Closer(spell_group=enemy_spell_group) for i in range(3)])
    while running:
        frame = frame % 60 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (inventory_ui.get_click(event.pos) is not None) or (wand_ui.get_click(event.pos) is not None):
                    inventory_chose = inventory_ui.get_click(event.pos) if inventory_ui.get_click(
                        event.pos) is not None else inventory_chose
                    wand_chose = wand_ui.get_click(event.pos) if wand_ui.get_click(event.pos) is not None else wand_chose
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
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    size = screen.get_size()
        if pygame.sprite.spritecollideany(player, exit_group):
            return True

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
                player.cast((left, top), spell_group=spell_group, vec=vec)
                cooldown_time = time()

        casting = True if spell_group else False
        board.render()
        left += (b_mose_pos[0] - mouse_pos[0]) / 70
        top += (b_mose_pos[1] - mouse_pos[1]) / 70
        board.update(left, top)
        wizard.update(any([keys[i] for i in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)]))
        player.image = wizard.image
        player.render(screen)
        player.update(center=(player.rect.center[0] + (b_mose_pos[0] - mouse_pos[0]) / 70,
                              player.rect.center[1] + (b_mose_pos[1] - mouse_pos[1]) / 70))
        b_mose_pos = (
            b_mose_pos[0] - (b_mose_pos[0] - mouse_pos[0]) / 5, b_mose_pos[1] - (b_mose_pos[1] - mouse_pos[1]) / 5)

        if keys[pygame.K_c]:
            zoom += 0.05
        if keys[pygame.K_x]:
            if zoom - 0.1 > 0.1:
                zoom -= 0.05

        bolt.update(casting)
        spell_group.update(map_move=(left, top), anim=bolt.image)
        spell_group.draw(screen)
        enemy_group.update(map_move=(left, top), player=player)
        enemy_group.draw(screen)
        enemy_spell_group.update(map_move=(left, top))
        enemy_spell_group.draw(screen)

        scr = pygame.transform.scale(pygame.display.get_surface(), (width * zoom, height * zoom)), (
            width / 2 * (1 - zoom), height / 2 * (1 - zoom))
        screen.blit(pygame.transform.scale(load_image('fon.png'), (width, height)), (0, 0))
        screen.blit(*scr)
        inventory_ui.render()
        wand_ui.render()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
    pygame.display.flip()



# while start_game() is False:
#     while start_game() is True:
#         start_game()
