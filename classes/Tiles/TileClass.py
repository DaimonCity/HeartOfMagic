import pygame
from scripts.image_scripts import *
class Tile(pygame.sprite.Sprite):
    sprite = 'test_image.jpg'
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.sprite = Tile.sprite
        self.image = load_image(self.sprite)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
    def render(self, screen, x, y, board):
        self.rect.x, self.rect.y = x * board.cell_size + board.left, y * board.cell_size + board.top


