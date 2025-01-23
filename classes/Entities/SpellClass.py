import pygame.draw

from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
class Spell(Entity):
    def __init__(self):
        super().__init__('test_image.jpg')
        self.existence = False
        self.center = (0, 0)

    def update(self, properties=None):
        if properties != None:
            self.rect.center = properties.center
    def cast(self, summoner):
        self.center = summoner.rect.center
        print(1)
        self.fire()
        self.update(self)
    def fire(self):
        pass






class Spell2(Spell):
    def __init__(self, summoner):
        print(super())
        super().__init__('spell_png')
    def fire(self):
        print(2)