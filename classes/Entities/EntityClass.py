import pygame.sprite
from scripts.image_scripts import *
from time import time

class Entity(pygame.sprite.Sprite):
    def __init__(self, board, image='entity.png'):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.spell_line = None
        self.summoner = None
        self.damage_cooldown_timer = None
        self.hp = None
        self.damage_cooldown_timer = None
        self.damage = 0
        self.image = load_image(image, -1)
        self.board = board
        self.rect = self.image.get_rect(center=(0, 0))
        self.speed = 0
        self.center = self.rect.center
        self.vec = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def collide_damage(self, colizer, map_move, board, kill=0):
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer):
                if time() - self.damage_cooldown_timer >= 0.5:
                    self.hp -= colizer.damage
                    if colizer.damage != 0:
                        self.damage_cooldown_timer = time()
                    print(self.hp)
                    if kill:
                        colizer.summon(map_move=map_move, board=board)
                        colizer.kill()

    def summon(self, map_move, board):
        if len(self.spell_line) != 0:
            spell = self.spell_line[0](board)
            if self.groups():
                self.groups()[0].add(spell)
                spell.cast(map_move=map_move, summoner=self, vec=self.vec, spell_line=self.spell_line[1:], board=board)

    def leave_rule(self, map_move, board):
        pass

    def move(self, map_move, board, center=None, funx=0, funy=0):
        backup = self.center
        self.rect.center = (
            self.rect.center[0] + self.vec[0] * self.speed, self.rect.center[1] + self.vec[1] * self.speed)
        if center is not None:
            self.center = center[0] - map_move[0] + self.vec[0] * 25, center[1] - map_move[1] + self.vec[1] * 25
            self.vec = (self.vec[0] + self.summoner.vec[0] * self.summoner.speed,
                        self.vec[1] * self.summoner.speed + self.summoner.vec[1])
        self.center = (self.center[0] + self.vec[0] * self.speed + funx,
                       self.center[1] + self.vec[1] * self.speed + funy)
        self.rect.center = (self.center[0] + map_move[0],
                            self.center[1] + map_move[1])

    def update(self, board, center=None, map_move=(0, 0), anim=None):
        self.leave_rule(map_move, board=board)
        self.move(map_move=map_move, center=center, board=board)
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


class HpBar(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, player, screen):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.player = player
        self.size = self.height, self.width = screen.get_height(), screen.get_width()
        self.screen = screen
        self.hp_bar = pygame.sprite.Group()

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = 202 - self.player.hp
        if self.player.hp <= 0:
            self.image = self.frames[-1]
        else:
            self.image = self.frames[self.cur_frame]

        self.screen.blit(pygame.transform.scale(self.image, (256 * 3, 32 * 3)),
                         (self.screen.get_rect().bottomleft[0] + 20, self.screen.get_rect().bottomleft[1] - 3 * 48,
                          256 * 3,
                          32 * 3))
