import pygame
from classes.Entities.FreeplaceClass import Freeplace
from classes.Entities.EntityClass import Entity
from scripts.image_scripts import load_image
from classes.Entities.SpellClass import *


class Hero(Entity):
    def init(self, screen):
        super().init()
        self.image = load_image('player.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.speed = 7

    def update(self, center=None, rect=None):
        if center is not None:
            self.rect.center = center
        if rect is not None:
            self.rect.update(rect)

    def move(self, vec, left, top, screen, board):  # Принимаем board
        if vec == (0, 0):
            return left, top

        freplace = Freeplace(screen, vec, self)
        cof_x, cof_y = 1, 1
        if (vec[0] >= 0) == (self.rect.center[0] - screen.get_width() // 2 >= 0):
            cof_x = min(self.rect.x - freplace.rect.x, freplace.rect.x + freplace.rect.width - self.rect.x) / freplace.rect.width * 2
        if (vec[1] >= 0) == (self.rect.center[1] - screen.get_height() // 2 >= 0):
            cof_y = min(self.rect.y - freplace.rect.y, freplace.rect.y + freplace.rect.height - self.rect.y) / freplace.rect.height * 2

        x = self.rect.center[0] + vec[0] * self.speed * cof_x
        y = self.rect.center[1] + vec[1] * self.speed * cof_y

        temp_rect = self.rect.copy()
        temp_rect.center = (x, y)
        for row in board.board:
            for tile in row:
                if isinstance(tile, WallTile):
                    if temp_rect.colliderect(tile.rect):
                        if vec[0] > 0:  # Движение вправо
                            x = tile.rect.left - temp_rect.width // 2
                        elif vec[0] < 0:  # Движение влево
                            x = tile.rect.right + temp_rect.width // 2
                        if vec[1] > 0:  # Движение вниз
                            y = tile.rect.top - temp_rect.height // 2
                        elif vec[1] < 0:  # Движение вверх
                            y = tile.rect.bottom + temp_rect.height // 2
                        break
            else:
                continue
            break

        self.update(center=(x, y))

        left -= vec[0] * self.speed * (1 - cof_x)
        top -= vec[1] * self.speed * (1 - cof_y)

        return left, top

    def cast(self, map_move, spell_group, vec):
        spell_line = [Spell, Spell2, Spell2, Spell, Spell3, Spell5]
        spell = spell_line[0]()
        spell_group.add(spell)
        spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=spell_line[1:])