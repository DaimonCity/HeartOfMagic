import random
import pygame.draw
from time import time
from classes.Entities.EntityClass import Entity
from scripts.image_scripts import *
import math


class Vacous(Entity):
    def __init__(self, board, image='woid.jpg', logo='Empty_slot.png'):
        super().__init__(image=image, board=board)
        self.spell_line = []
        self.live_time = 0.1
        self.live_timer = time()
        self.logo = pygame.transform.scale(load_image(logo), (32 * 3, 32 * 3))
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(center=(0, 0))

    def leave_rule(self, map_move, board):
        if time() - self.live_timer >= self.live_time:
            self.summon(map_move=map_move, board=board)
            self.kill()

    def update(self, board, center=None, map_move=(0, 0), anim=None):
        self.leave_rule(map_move, board=board)
        self.move(map_move=map_move, center=center, board=board)



class Spell(Entity):
    def __init__(self, board, image='Bolt.png', logo='test_image.jpg'):
        super().__init__(image=image, board=board)
        self.spell_line = []
        self.logo = pygame.transform.scale(load_image(logo), (32 * 3, 32 * 3))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 4
        self.live_time = 3
        self.live_timer = time()
        self.damage = 5

    def leave_rule(self, map_move, board):
        if time() - self.live_timer >= self.live_time:
            self.summon(map_move=map_move, board=board)
            self.kill()
        if pygame.sprite.spritecollideany(self, board.collide_group):
            self.vec = (-self.vec[0], -self.vec[1])
            self.summon(map_move=map_move, board=board)
            self.kill()
    def update(self, board, center=None, map_move=(0, 0), anim=None):
        super().update(board, center, map_move, anim)
        # if self.__class__.__name__ == 'Unstable':
        #     for x in range(self.image.get_width()):
        #         for y in range(self.image.get_height()):
        #             if self.image.get_at((x, y))[3] != 0:
        #                 self.image.set_at((x, y), pygame.Color(random.randrange(255), random.randrange(255),
        #                                                        random.randrange(255)))
        # if self.__class__.__name__ == 'Bolt':
        #     for x in range(self.image.get_width()):
        #         for y in range(self.image.get_height()):
        #             if self.image.get_at((x, y))[3] != 0:
        #                 self.image.set_at((x, y), pygame.Color(random.randrange(127, 255), random.randrange(255),
        #                                                        random.randrange(127, 255)))
        # if self.__class__.__name__ == 'Sin':
        #     for x in range(self.image.get_width()):
        #         for y in range(self.image.get_height()):
        #             if self.image.get_at((x, y))[3] != 0:
        #                 self.image.set_at((x, y), pygame.Color(random.randrange(255), 0, 0))

class Bolt(Spell):
    def __init__(self, board, image='Bolt.png', logo='Bolt_icon.png'):
        super().__init__(image=image, logo=logo, board=board)


class Unstable(Spell):
    def __init__(self, board, image='Bolt.png', logo='Unstab_icon.png'):
        super().__init__(image=image, logo=logo, board=board)
        self.speed = 2

    def move(self, map_move, center, board):
        super().move(board=board, map_move=map_move, center=center, funx=random.randrange(-5, 5),
                     funy=random.randrange(-5, 5))


class Sin(Spell):
    def __init__(self, board, image='Bolt.png', logo='Sin_icon.png'):
        super().__init__(image=image, logo=logo, board=board)
        self.speed = 5

    def move(self, map_move, center, board):
        super().move(board=board, map_move=map_move, center=center, funx=math.sin(time() * 10) * 10 * self.vec[1],
                     funy=-math.sin(time() * 10) * 10 * self.vec[0])


class Triple(Spell):
    def __init__(self, board, logo='triple_icon.png'):
        super().__init__(logo=logo, board=board)
        self.live_time = 0.001

    def summon(self, map_move, board):
        if len(self.spell_line) != 0:
            for i in range(3 if len(self.spell_line) >= 3 else len(self.spell_line)):
                spell = self.spell_line[i](board)
                self.groups()[0].add(spell)
                vec = normolize_vec((self.vec[0] + ((i - 1) / 3), self.vec[1] + ((i - 1) / 3)))
                spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[3:], board=board)
