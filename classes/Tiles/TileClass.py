import pygame
from scripts.image_scripts import *
class Tile(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('test_image.jpg')
        self.add(group)
        self.rect = self.image.get_rect(center=(100, 0))
    def render(self, screen, x, y, board):
        #self.rect.x, self.rect.y = x * board.cell_size + board.left, y * board.cell_size + board.top
        self.rect.update(x * board.cell_size + board.left, y * board.cell_size + board.top, board.cell_size, board.cell_size)
        #pygame.draw.rect(screen, (255, 255 * (y % 2), 255 * (x % 2)), self.rect, x + y + 1)

