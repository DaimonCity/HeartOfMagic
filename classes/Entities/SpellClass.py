import random
import pygame.draw
from time import time
from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
import math


class Vacous(Entity):
    def __init__(self, image='test_image.jpg', logo='Empty_slot.png'):
        super().__init__(image)
        self.spell_line = []
        self.logo = pygame.transform.scale(load_image(logo), (32 * 3, 32 * 3))
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(center=(0, 0))
    def leave_rule(self, map_move):
        self.summon(map_move=map_move)
        self.kill()
class Spell(Entity):
    def __init__(self, image='Bolt.png', logo='test_image.jpg'):
        super().__init__(image)
        self.spell_line = []
        self.logo = pygame.transform.scale(load_image(logo), (32 * 3, 32 * 3))
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 4
        self.live_time = 3
        self.live_timer = time()
    def leave_rule(self, map_move):
        if time() - self.live_timer >= self.live_time:
            self.summon(map_move=map_move)
            self.kill()
class Bolt(Spell):
    def __init__(self, image='Bolt.png', logo='Door.png'):
        super().__init__(image=image, logo=logo)


class Unstable(Spell):
    def __init__(self, image='Bolt.png', logo='entity.png'):
        super().__init__(image, logo=logo)
        self.speed = 2


    def move(self, map_move, center):
        super().move(map_move, center, funx=random.randrange(-5, 5),
                                       funy=random.randrange(-5, 5))

class Sin(Spell):
    def __init__(self, image='Bolt.png', logo='Floor.png'):
        super().__init__(image, logo=logo)
        self.speed = 5

    def move(self, map_move, center):
        super().move(map_move, center, funx=math.sin(time() * 10) * 10 * self.vec[1],
                                       funy=-math.sin(time() * 10) * 10 * self.vec[0])

class Triple(Spell):
    def __init__(self, logo='test_image.jpg'):
        super().__init__(logo=logo)
        self.live_time = 0.001
    def summon(self, map_move):
        if len(self.spell_line) != 0:
            for i in range(3 if len(self.spell_line) >= 3 else len(self.spell_line)):
                spell = self.spell_line[i]()
                self.groups()[0].add(spell)
                vec = normolize_vec((self.vec[0] +  ((i - 1) / 3), self.vec[1] + ((i - 1) / 3)))
                spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[3:])
