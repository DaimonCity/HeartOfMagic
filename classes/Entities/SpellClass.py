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
        self.existence = False
        self.center = (0, 0)

    def update(self, center=None, vec=None, map_move=(0,0)):
        if center != None:
            self.rect.center = center
        if vec != None:
            self.rect.center = self.rect.center[0] + vec[0] * 100, self.rect.center[1] + vec[1] * 100
        self.rect.center


    def cast(self, summoner, vec):
        self.summoner = summoner
        self.update(center=summoner.rect.center)
        self.fire(vec, summoner)
    def fire(self, vec, summoner):
        vec = vec[0] - self.summoner.rect.center[0], vec[1] - self.summoner.rect.center[1]
        vec = vec[0] / max(map(abs,vec)) , vec[1] / max(map(abs,vec))
        self.update(vec=vec)


class Spell2(Spell):
    def __init__(self):
        super().__init__(image='test_image.jpg')

    def fire(self, vec):
        super().fire(vec)
        self.update()
        print(1)