from classes.Entities.FreeplaceClass import Freeplace
from classes.Entities.SpellClass import *


class Hero(Entity):
    def __init__(self, screen, hero):
        super().__init__()
        self.image = hero.image
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.speed = 7
        self.spell_line = []
        self.spell = None

    def update(self, center=None, rect=None):
        if center is not None:
            self.rect.center = center
        if rect is not None:
            self.rect.update(rect)

    def to_move(self, vec, left, top, screen, coliders=0):
        free_place = Freeplace(screen, vec, self)
        cof_x, cof_y = 1, 1
        if (vec[0] >= 0) == (self.rect.center[0] - screen.get_width() // 2 >= 0):
            cof_x = min(self.rect.x - free_place.rect.x,
                        free_place.rect.x + free_place.rect.width - self.rect.x) / free_place.rect.width * 2
        if (vec[1] >= 0) == (self.rect.center[1] - screen.get_height() // 2 >= 0):
            cof_y = min(self.rect.y - free_place.rect.y,
                        free_place.rect.y + free_place.rect.height - self.rect.y) / free_place.rect.height * 2
        x = self.rect.center[0] + vec[0] * self.speed * cof_x
        y = self.rect.center[1] + vec[1] * self.speed * cof_y
        self.update(center=(x, y))
        left -= vec[0] * self.speed * (1 - cof_x)
        top -= vec[1] * self.speed * (1 - cof_y)
        return left, top

    def cast(self, map_move, spell_group, vec):
        self.spell_line = [Spell, Spell2, Spell2, Spell, Spell3, Spell5]
        self.spell = self.spell_line[0]()
        spell_group.add(self.spell)
        self.spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[1:])
