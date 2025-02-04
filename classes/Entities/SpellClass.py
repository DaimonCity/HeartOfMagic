import random

import pygame.draw
from time import time
from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
import math
import math


def reduce_fraction(n, m):
    k = math.gcd(n, m)
    return n // k, m // k


class Spell(Entity):
    def __init__(self, image='test_image.jpg'):
        super().__init__(image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(0, 0))
        self.vec = (0, 0)
        self.speed = 4
        self.live_time = 3
        self.live_timer = time()
        self.center = None
        self.spell_line = None

    def leave_rule(self, map_move):
        if time() - self.live_timer >= self.live_time:
            if len(self.spell_line) != 0:
                spell = self.spell_line[0]()
                self.groups()[0].add(spell)
                spell.cast(map_move=map_move, summoner=self, vec=self.vec, spell_line=self.spell_line[1:])
            self.kill()

    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed, self.center[1] + self.vec[1] * self.speed
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]

    def update(self, center=None, map_move=(0, 0)):
        self.leave_rule(map_move)
        self.move(map_move, center)

    def cast(self, map_move, summoner, vec, spell_line):
        self.spell_line = spell_line
        self.update(center=summoner.rect.center, map_move=map_move)
        self.fire(vec, summoner)

    def fire(self, vec, summoner):
        if summoner.__class__.__name__ == 'Hero':
            vec = vec[0] - summoner.rect.center[0], vec[1] - summoner.rect.center[1]
            if max(vec) != 0:
                vec = vec[0] / max(map(abs, vec)), vec[1] / max(map(abs, vec))
                self.vec = vec
        else:
            self.vec = vec


class Spell5(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 1


class Spell2(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 1

    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed, self.center[1] + self.vec[
            1] * self.speed + random.randrange(-10, 10)
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]


class Spell3(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 5

    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed + math.sin(time() * 10) * 10 * self.vec[1], self.center[
            1] + self.vec[1] * self.speed - math.sin(time() * 10) * 10 * self.vec[0]
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]


class Spell4(Spell):
    def __init__(self, image='player.png'):
        super().__init__(image)
        self.speed = 5

    def move(self, map_move, center):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = self.center[0] + self.vec[0] * self.speed + math.sin(time() * 10) * 10 * self.vec[1], self.center[
            1] + self.vec[1] * self.speed - math.cos(time() * 10) * 10 * self.vec[0]
        self.rect.center = self.center[0] + map_move[0], self.center[1] + map_move[1]
