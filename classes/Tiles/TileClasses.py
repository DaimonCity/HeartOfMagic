import pygame
from scripts.image_scripts import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, image='empty.png', colorkey=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image, colorkey)
        self.cons_image = self.image
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, x, y, board):
        self.image = pygame.transform.scale(self.cons_image, (board.cell_size, board.cell_size))
        self.rect.update(x * board.cell_size + board.left, y * board.cell_size + board.top, board.cell_size, board.cell_size)


class WallTile(Tile):
    def __init__(self):
        super().__init__('wall.png')

class FloorTile(Tile):
    def __init__(self):
        super().__init__('floor.png')
class WoidTile(Tile):
    def __init__(self):
        super().__init__('woid.jpg', -1)


