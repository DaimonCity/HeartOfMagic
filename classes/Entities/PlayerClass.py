import pygame
from classes.Entities.FreeplaceClass import Freeplace
from classes.Entities.EntityClass import Entity
from  scripts.image_scripts import load_image
from classes.Entities.SpellClass import *
class Hero(Entity):
    def __init__(self, screen):
        super().__init__()
        self.image = load_image('player.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.speed = 7
        self.rect.height
    def update(self, center=None):
        if center != None:
            self.rect.center = center
    def move(self, vec, left, top, screen, coliders=0):
        freplace = Freeplace(screen, vec, self)
        cof_x, cof_y = 1, 1
        if (vec[0] >= 0) == (self.rect.center[0] - screen.get_width() // 2 >= 0):
            cof_x = min(self.rect.x - freplace.rect.x, freplace.rect.x + freplace.rect.width - self.rect.x) / freplace.rect.width * 2
        if (vec[1] >= 0) == (self.rect.center[1] - screen.get_height() // 2 >= 0):
            cof_y = min(self.rect.y - freplace.rect.y, freplace.rect.y + freplace.rect.height - self.rect.y) / freplace.rect.height * 2
        x = self.rect.center[0] + vec[0] * self.speed * cof_x
        y = self.rect.center[1] + vec[1] * self.speed * cof_y
        self.update(center=(x, y))
        left -= vec[0] * self.speed * (1 - cof_x)
        top -= vec[1] * self.speed * (1 - cof_y)
        return left, top

    def cast(self, spell_group, vec):
        spell_line = [Spell, Spell]
        for spell in spell_line:
            spell = spell()
            spell_group.add(spell)
            spell.cast(summoner=self, vec=vec)

