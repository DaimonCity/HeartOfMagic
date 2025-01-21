import pygame.transform
from classes.Entities.FreeplaceClass import Freeplace
from classes.Entities.EntityClass import Entity
from  scripts.image_scripts import load_image
class Hero(Entity):
    def __init__(self, screen):
        super().__init__()
        self.image = load_image('entity.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.cons_rect.size = (64, 64)
        print(self.rect.center)
        self.rect.center = (screen.get_width(), screen.get_height() / 2)
    def move(self, vec, left, top, screen, coliders=0):
        freplace = Freeplace(screen, vec, self)
        pygame.draw.rect(screen, (255, 255, 255), freplace.rect)
        x_move_t = freplace.rect.x < self.rect.x < freplace.rect.x + freplace.rect.width
        y_move_t = freplace.rect.y < self.rect.y < freplace.rect.y + freplace.rect.height
        if x_move_t:
            self.rect.x = self.rect.x + vec[0] * self.speed
        else:
            left -= vec[0] * self.speed
        if y_move_t:
            self.rect.y = self.rect.y + vec[1] * self.speed
        else:
            top -= vec[1] * self.speed
        return left, top