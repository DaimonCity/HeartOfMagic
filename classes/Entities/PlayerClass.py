from classes.Entities.SpellClass import *


class Hero(Entity):
    def __init__(self, screen, hero, board):
        super().__init__(board=board)
        self.image = hero.image
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.spell_line = [Vacous()]
        self.speed = 7
        self.cooldown = 0.5
        self.mose_pose = (0, 0)
        self.spell_line = [Vacous()]
        self.spell = None

    def update(self, center=None, rect=None):
        if center is not None:
            self.rect.center = center
        if rect is not None:
            self.rect.update(rect)

    def move(self, vec, left, top, screen, mose_pos=(0, 0)):
        backup = (left, top)
        left -= vec[0] * self.speed
        top -= vec[1] * self.speed
        if self.board != 0:
            if pygame.sprite.spritecollideany(self, self.board.collide_group):
                return backup
        return left, top

    def cast(self, map_move, spell_group, vec):
        # self.spell_line = [Triple, Unstable, Bolt, Sin]
        spell = self.spell_line[0]()
        spell_group.add(spell)
        spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=self.spell_line[1:], board=self.board)
