from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Generation.generation_floor import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 832
    screen = pygame.display.set_mode(size)

    floor = Map(EMPTY_MAP)
    _y = choice_cord(1, len(floor.map) - 1)
    floor.set_one_sprite(0, _y, 14)
    floor.draw_line((1, _y), 'x', 'right')
    tiles_dict = {0: FloorTile(), 1: WallTile(), 2: DoorTile(), 3: UpperLeftCornerTile(), 4: UpperLeftCornerTile(),
                  5: DownerLeftCornerTile(), 6: UpperRightCornerTile(), 7: DownerRightCornerTile(),
                  8: LeftWallTile(), 9: TToUpTile(), 11: RightWallTile(), 12: TToAllTile(), 13: TToDownTile(),
                  14: TLeftWallTile(), 15: TRightWallTile(), 16: TLeftWallForRoomTile(), 17: SideDoorTile()}

    _map = floor.get_map()
    pprint(_map)
    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.get_click(event.pos)
        board.render()
        pygame.display.update()
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.display.flip()
