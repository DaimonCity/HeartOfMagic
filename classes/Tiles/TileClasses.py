import pygame
from scripts.image_scripts import *


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('test_image.jpg')
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, x, y, board):
        self.image = pygame.transform.scale(self.image, (board.cell_size, board.cell_size))
        self.rect.update(x * board.cell_size + board.left, y * board.cell_size + board.top, board.cell_size, board.cell_size)


class WallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('wall.png')

class FloorTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('floor.png')

