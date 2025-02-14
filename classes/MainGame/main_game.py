import pygame.sprite

from classes.Animations.AnimationsClasses import AnimatedSprite
from classes.Boards.BoardClass import UI, Board
from classes.Entities.EnemyClass import Ranger, Closer
from classes.Entities.PlayerClass import Hero
from classes.Entities.SpellClass import *
from classes.Generation.generation_floor import Map, choice_cord, EMPTY_MAP
from classes.Tiles.TileClasses import *

FPS = 60


def make_room():
    floor = Map(EMPTY_MAP)
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    spawn = floor.add_exit()

    _map = floor.get_map()

    top, left = spawn


def start_game(top, left, ex_g, sp_g, en_g, enp_g, screen, _map, inventory_ui, inv_chose, wand_ui, player,
               running=True, frame=0, zoom=3):
    bolt = AnimatedSprite(load_image("Bolt-Sheet.png"), 9, 1, 32 * 8, 32)
    screen.get_width()
    animation_of_magic = {Spell: bolt}
    clock = pygame.time.Clock()
    keys = dict()
    keyboard = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_x, pygame.MOUSEBUTTONDOWN)
    b_mose_pos = screen.get_rect().center
    tiles_dict = {0: FloorTile(), 1: WallTile(), 2: DoorTile(), 3: UpperLeftCornerTile(), 4: UpperLeftCornerTile(),
                  5: DownerLeftCornerTile(), 6: UpperRightCornerTile(), 7: DownerRightCornerTile(),
                  8: LeftWallTile(), 9: TToUpTile(), 11: RightWallTile(), 12: TToAllTile(), 13: TToDownTile(),
                  14: TLeftWallTile(), 15: TRightWallTile(), 16: TLeftWallForRoomTile(), 17: SideDoorTile(), 20: Void()}

    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=64)
    player.spell_line = [i.__class__ for i in wand_ui.board[0]]
    cooldown_time = time()
    for i in keyboard:
        keys[i] = 0
    while running:
        frame = frame % 60 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (inventory_ui.get_click(event.pos) is not None) or (wand_ui.get_click(event.pos) is not None):
                    inv_chose = inventory_ui.get_click(event.pos) if inventory_ui.get_click(
                        event.pos) is not None else inv_chose
                    wnd_chose = wand_ui.get_click(event.pos) if wand_ui.get_click(event.pos) is not None else wnd_chose
                    if (inv_chose is not None) and (wnd_chose is not None):
                        inventory_ui.board[inv_chose[1]][inv_chose[0]], wand_ui.board[wnd_chose[1]][
                            wnd_chose[0]] = wand_ui.board[wnd_chose[1]][wnd_chose[0]], \
                            inventory_ui.board[inv_chose[1]][inv_chose[0]]
                        player.spell_line = [i.__class__ for i in wand_ui.board[0]]
                        inv_chose = None
                        wnd_chose = None

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

        if pygame.sprite.spritecollideany(player, ex_g):
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
        sp_g.update(map_move=(left, top), anim=bolt.image)
        sp_g.draw(screen)
        en_g.update(map_move=(left, top), player=player)
        en_g.draw(screen)
        enp_g.update(map_move=(left, top))
        enp_g.draw(screen)

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


# game = start_game(exit_group)
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    scrn = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  #
    size = width, height = scrn.get_size()
    wizard = AnimatedSprite(load_image("ToDownMag-Sheet.png"), 8, 1, 32 * 8, 32)
    player = Hero(scrn, wizard)

    w_ui = UI(screen=scrn, any_map=['0000'], tiles_dict={'0': Vacous()}, left=10, top=0, cell_size=32 * 3)
    i_ui = UI(screen=scrn, any_map=['00000'], tiles_dict={'0': Bolt()}, left=scrn.get_width() - 32 * 3 * 5,
              top=0, cell_size=32 * 3)
    print(w_ui.board)
    i_ui.board = [[Triple(), Bolt(), Unstable(), Sin(), Vacous(), Vacous()]]
    inventory_chose = None
    wand_chose = None

    spell_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_spell_group = pygame.sprite.Group()
    enemy_group.add([Ranger(spell_group=enemy_spell_group) for i in range(3)])
    enemy_group.add([Closer(spell_group=enemy_spell_group) for i in range(3)])
    exit_group = pygame.sprite.Group()
