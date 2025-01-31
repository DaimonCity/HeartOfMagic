from scripts.image_scripts import *
from time import time

class Entity(pygame.sprite.Sprite):
    def __init__(self, image='entity.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image)
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 0
        self.vec = (0, 0)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def summon(self, map_move):
        if len(self.spell_line) != 0:
            spell = self.spell_line[0]()
            self.groups()[0].add(spell)
            spell.cast(map_move=map_move, summoner=self, vec=self.vec, spell_line=self.spell_line[1:])
    def leave_rule(self, map_move):
        pass

    def move(self, map_move, center=None):
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
        self.center = (self.center[0] + self.vec[0] * self.speed,
                       self.center[1] + self.vec[1] * self.speed)
        self.rect.center = (self.center[0] + map_move[0],
                            self.center[1] + map_move[1])

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
            self.vec = normolize_vec(vec)
        else:
            self.vec = vec