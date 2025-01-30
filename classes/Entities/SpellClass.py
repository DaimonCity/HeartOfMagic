import random

import pygame.draw
from time import time
from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
import math


class Spell(Entity):
    def __init__(self, image='test_image.jpg'):
        super().__init__(image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 4
        self.live_time = 3
        self.live_timer = time()
    def leave_rule(self, map_move):
        if time() - self.live_timer >= self.live_time:
            self.summon(map_move=map_move)
            self.kill()


class Bolt(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)


class Unstable(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 1


    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed, self.center[1] + self.vec[
            1] * self.speed + random.randrange(-10, 10)
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]



class Sin(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 5

    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed + math.sin(time() * 10) * 10 * self.vec[1], self.center[
            1] + self.vec[1] * self.speed - math.sin(time() * 10) * 10 * self.vec[0]
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]



class Triple(Spell):
    def __init__(self):
        super().__init__()
        self.live_time = 0.001
    def summon(self, map_move):
        if len(self.spell_line) != 0:

            for i in range(3 if len(self.spell_line) >= 3 else len(self.spell_line)):
                spell = self.spell_line[i]()
                self.groups()[0].add(spell)
                vec = normolize_vec((self.vec[0] +  ((i - 1) / 3), self.vec[1] + ((i - 1) / 3)))
                spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[3:])
