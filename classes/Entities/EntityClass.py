import pygame
from scripts.image_scripts import load_image
from  copy import copy
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('entity.png')
        self.cons_image = self.image
        self.rect = self.image.get_rect(center=(0, 0))
        self.cons_rect = copy(self.rect)
        self.speed = 10
    def move(self, vec):
        self.rect.move(self.rect.x + vec[0] * self.speed, self.rect.y + vec[1] * self.speed)
        self.rect.x, self.rect.y = self.rect.x + vec[0] * self.speed, self.rect.y + vec[1] * self.speed
    def render(self, screen):
        screen.blit(self.image, self.rect)
    def update(self, zoom):
        self.rect.size = (self.cons_rect.width * zoom, self.cons_rect.height * zoom)
        # self.rect.center = (self.rect.center[0] + zoom, self.rect.center[1] + zoom)
        self.image = pygame.transform.scale(self.cons_image, self.rect.size)