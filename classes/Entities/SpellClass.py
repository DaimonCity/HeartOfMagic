import pygame.draw

from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
import math

def reduce_fraction(n,m):
    k = math.gcd(n,m)
    return (n//k, m//k)

class Spell(Entity):
    def __init__(self, image='test_image.jpg'):
        super().__init__(image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(0, 0))
        self.vec = (0, 0)
        self.speed = 3
    def update(self, center=None, map_move=(0, 0)):
        if center != None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed, self.center[1] + self.vec[1] * self.speed
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]


    def cast(self,map_move, summoner, vec):
        self.update(center=summoner.rect.center, map_move=map_move)
        self.fire(vec, summoner)
    def fire(self, vec, summoner):
        vec = vec[0] - summoner.rect.center[0], vec[1] - summoner.rect.center[1]
        vec = vec[0] / max(map(abs,vec)) , vec[1] / max(map(abs,vec))
        self.vec = vec


class Spell2(Spell):
    def __init__(self):
        super().__init__(image='test_image.jpg')

    def fire(self, vec):
        super().fire(vec)
        self.update()
        print(1)