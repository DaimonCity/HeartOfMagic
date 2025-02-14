import pygame

from classes.Generation.generation_floor import objects
from scripts.image_scripts import load_image
from copy import copy
import pygame.sprite
from scripts.image_scripts import *
from time import time


class Entity(pygame.sprite.Sprite):
    def __init__(self, board, image='entity.png'):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = load_image(image, -1)
        self.board = board
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 0
        self.center = self.rect.center
        self.vec = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def summon(self, map_move, board):
        if len(self.spell_line) != 0:
            spell = self.spell_line[0](board)
            self.groups()[0].add(spell)
            spell.cast(map_move=map_move, summoner=self, vec=self.vec, spell_line=self.spell_line[1:], board=board)

    def leave_rule(self, map_move, board):
        pass

    def move(self, map_move, center=None, funx=0, funy=0):
        backup = self.center
        self.rect.center = (self.rect.center[0] + self.vec[0] * self.speed, self.rect.center[1] + self.vec[1] * self.speed)
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
            self.vec = (self.vec[0] + self.summoner.vec[0] * self.summoner.speed,
                        self.vec[1] * self.summoner.speed + self.summoner.vec[1])
        self.center = (self.center[0] + self.vec[0] * self.speed + funx,
                       self.center[1] + self.vec[1] * self.speed + funy)
        self.rect.center = (self.center[0] + map_move[0],
                            self.center[1] + map_move[1])

        # if pygame.sprite.spritecollideany(self, self.board.collide_group) is not None:
        #     self.rect.center = backup

    def update(self, board, center=None, map_move=(0, 0), anim=None):
        self.leave_rule(map_move, board=board)
        self.move(map_move=map_move, center=center)
        if anim is not None:
            self.image = anim
    def cast(self, map_move, summoner, vec, spell_line, board):
        self.summoner = summoner
        self.spell_line = spell_line
        self.update(center=summoner.rect.center, map_move=map_move, board=board)
        self.fire(vec, summoner)

    def fire(self, vec, summoner):
        if summoner.__class__.__name__ == 'Hero':
            vec = vec[0] - summoner.rect.center[0], vec[1] - summoner.rect.center[1]
            self.vec = normolize_vec(vec)
        else:
            self.vec = vec