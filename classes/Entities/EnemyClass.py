from classes.Entities.EntityClass import Entity
from random import randint
from scripts.image_scripts import *
from time import time


class Enemy(Entity):
    def __init__(self, image='entity.png'):
        super().__init__(image='entity.png')
        self.point = (100, 100)
        self.speed = 7
        self.speed_const = self.speed
        self.sleep = 0.5
        self.sleep_timer = time()
        self.center = self.rect.center
        self.logica = lambda :(randint(0, 500), randint(0, 500))

    def update(self, map_move):
        if time() - self.sleep_timer <= self.sleep:
            self.speed = 0
        else:
            self.speed = self.speed_const
        if (abs(self.rect.center[0] - self.point[0] - map_move[0]) <= self.speed + 1) and (abs(self.rect.center[1] - self.point[1] - map_move[1]) <= self.speed + 1):
            self.point = self.logica()
            self.sleep_timer = time()
        vec = (self.point[0] - self.rect.center[0] + map_move[0],
               self.point[1] - self.rect.center[1] + map_move[1])

        self.vec = normolize_vec((vec))
        super().update(map_move=map_move)

class Closer(Enemy):
    def __init__(self):
        super().__init__(image='entity.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(0, 0))
    def update(self, map_move, player):
        self.logica = lambda :(randint(*sorted([self.rect.center[0] - int(map_move[0]), player.rect.center[0] - int(map_move[0])])),
                               randint(*sorted([self.rect.center[1] - int(map_move[1]), player.rect.center[1] - int(map_move[1])])))
        super().update(map_move)
