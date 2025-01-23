import pygame.transform
from classes.Entities.FreeplaceClass import Freeplace
from classes.Entities.EntityClass import Entity
from  scripts.image_scripts import load_image
class Hero(Entity):
    def __init__(self, screen):
        super().__init__()
        self.image = load_image('player.png')
        self.cons_image = self.image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.cons_rect.size = (64, 64)
        self.speed = 7
    def move(self, vec, left, top, screen, coliders=0):
        freplace = Freeplace(screen, vec, self)
        cof_x = min(self.rect.x - freplace.rect.x, freplace.rect.x + freplace.rect.width - self.rect.x) / freplace.rect.width * 2
        cof_y = min(self.rect.y - freplace.rect.y, freplace.rect.y + freplace.rect.height - self.rect.y) / freplace.rect.height * 2
        self.rect.x = self.rect.x + vec[0] * self.speed * cof_x
        self.rect.y = self.rect.y + vec[1] * self.speed * cof_y
        left -= vec[0] * self.speed * (1 - cof_x)
        top -= vec[1] * self.speed * (1 - cof_y)
        return left, top