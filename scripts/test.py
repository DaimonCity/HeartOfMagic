from classes.Tiles.TileClasses import *
from classes.Boards.BoardClass import Board
from classes.Generation.generation_floor import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)

    tiles_dict = {1: WallTile(), 0: FloorTile(), 2: DoorTile()}
    floor = Map(EMPTY_MAP)
    floor.make_board()
    _y = choice_cord(1, len(floor.map) - 1)
    floor.draw_line((1, _y), 'x', 'right')
    floor.put_in_doors()

    _map = floor.get_map()
    board = Board(screen=screen, any_map=_map, tiles_dict=tiles_dict, left=10, top=20, cell_size=50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.get_click(event.pos)
        board.render(screen)
        pygame.display.update()
        pygame.display.flip()
        screen.fill(FloorTile())
    pygame.display.flip()
