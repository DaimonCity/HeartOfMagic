from classes.Entities.EntityClass import Entity
from random import randint
from scripts.image_scripts import *
class Enemy(Entity):
    def __init__(self):
        super().__init__(image='entity.png')
        self.point = (1000, 1000)
        self.speed = 1
    def update(self, map_move):
        if (abs(self.rect.center[0] - self.point[0]) <= self.speed) and (abs(self.rect.center[0] - self.point[0] <= self.speed)):
            self.point = (randint(0, 100), randint(0, 100))
            print(1)
        else:
            self.vec = normolize_vec((self.rect.center[0] - self.point[0], self.rect.center[0] - self.point[0]))
        super().update(map_move)