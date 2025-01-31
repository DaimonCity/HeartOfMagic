from classes.Entities.SpellClass import *


class Hero(Entity):
    def __init__(self, screen):
        super().__init__()
        self.image = load_image('player.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.speed = 7
        self.cooldown = 0.5
        self.mose_pose = (0, 0)
    def update(self, center=None, rect=None):
        if center is not None:
            self.rect.center = center
        if rect is not None:
            self.rect.update(rect)
    def move(self, vec, left, top, screen, mose_pos=(0, 0)):
        left -= vec[0] * self.speed
        top -= vec[1] * self.speed
        return left, top

    def cast(self, map_move, spell_group, vec):
        spell_line = [Bolt, Unstable, Sin, Bolt]
        spell = spell_line[0]()
        spell_group.add(spell)
        spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=spell_line[1:])