import pygame.sprite

from classes.Entities.SpellClass import *


class Hero(Entity):
    def __init__(self, screen, hero, board):
        super().__init__(board=board)
        self.image = hero.image
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.spell_line = [Vacous]
        self.speed = 7
        self.cooldown = 0.5
        self.mose_pose = (0, 0)
        self.damage_cooldown_timer = time()
        self.spell = None
        self.hp = 202

    def update(self, map_move, board, center=None, rect=None):
        if center is not None:
            self.rect.center = center
        if rect is not None:
            self.rect.update(rect)
        colizer = pygame.sprite.spritecollideany(self, self.board.enemy_group)
        self.collide_damage(colizer, map_move=map_move, board=board)
        colizer = pygame.sprite.spritecollideany(self, self.board.enemy_spell_group)
        self.collide_damage(colizer=colizer, kill=1, map_move=map_move, board=board)

    def move(self, vec, left, top, screen, mose_pos=(0, 0)):
        backup = (left, top)
        center = self.rect.center
        left -= vec[0] * self.speed
        top -= vec[1] * self.speed

        self.rect.center = (self.rect.center[0] + vec[0] * (self.speed * 2), center[1])
        colizer = pygame.sprite.spritecollideany(self, self.board.collide_group)
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer) is not None:
                left = backup[0]

        self.rect.center = (center[0], self.rect.center[1] + vec[1] * (self.speed * 2))
        colizer = pygame.sprite.spritecollideany(self, self.board.collide_group)
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer) is not None:
                top = backup[1]
        self.rect.center = center
        return left, top

    def cast(self, map_move, spell_group, vec, board):
        spell = self.spell_line[0](board)
        spell_group.add(spell)
        spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[1:], board=board)
