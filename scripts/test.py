import pygame
from classes.Tiles.TileClass import Tile
from classes.Boards.BoardClass import Board
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)

    base_tile = Tile()
    map_txt = '''#####
#####'''
    print(map_txt.split('\n'))
    map = [list(i) for i in map_txt.split('\n')]
    print(map)
    tiles_dict = {'#': base_tile}
    board = Board(map=map, tiles_dict=tiles_dict, left= 10, top= 20, cell_size=250)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.get_click(event.pos)
        board.render(screen)
        pygame.display.flip()
        #screen.fill((0, 0, 0))
    pygame.display.flip()
