import pygame
from classes.Tiles.TileClass import Tile
from classes.Boards.BoardClass import Board


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('HeartOfMagic')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    base_tile = Tile(all_sprites)
    tiles_dict = {'#': base_tile}
    map_txt = '''#####
#####
#####'''
    map = [list(i) for i in map_txt.split('\n')]
    board = Board(map=map, tiles_dict=tiles_dict, left= 10, top= 20, cell_size=50)
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
        screen.fill((0, 0, 0))
    pygame.display.flip()
