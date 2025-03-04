from random import randint
from classes.Entities.SpellClass import *


class Enemy(Entity):
    def __init__(self, spell_group, board, image='entity.png'):
        super().__init__(board=board, image=image)
        self.speed = 4
        self.board = board
        self.speed_const = self.speed
        self.sleep = 0.1
        self.sleep_timer = time()
        self.rect.center = (100, 100)
        self.center = self.rect.center
        self.logica = lambda: (randint(0, 1000), randint(0, 1000))
        self.spell_group = spell_group
        self.cooldown_time = time()
        self.cooldown_logica = lambda: randint(10, 30) / 10
        self.cooldown = self.cooldown_logica()
        self.point = self.rect.center

    def update(self, map_move, board):
        if time() - self.sleep_timer <= self.sleep:
            self.speed = 0
        else:
            self.speed = self.speed_const
        if (abs(self.rect.center[0] - self.point[0] - map_move[0]) <= self.speed + 1) and (
                abs(self.rect.center[1] - self.point[1] - map_move[1]) <= self.speed + 1):
            self.point = self.logica()
            self.sleep_timer = time()
        vec = (self.point[0] - self.rect.center[0] + map_move[0],
               self.point[1] - self.rect.center[1] + map_move[1])
        colizer = pygame.sprite.spritecollideany(self, self.board.player_spell_group)
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer) is not None:
                self.kill()
                colizer.summon(map_move=map_move, board=board)
                colizer.kill()

        self.vec = normolize_vec((vec))
        super().update(map_move=map_move, board=board)

    def move(self, map_move, board, center=None, funx=0, funy=0):
        backup = self.center
        super().move(map_move=map_move, board=board, center=center, funx=funx, funy=funy)
        self.rect.center = (self.center[0] + self.vec[0] * (self.speed * 2) + map_move[0], backup[1] + map_move[1])
        colizer = pygame.sprite.spritecollideany(self, self.board.collide_group)
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer) is not None:
                self.center = backup[0], self.center[1]
                self.point = self.logica()
        self.rect.center = (backup[0] + map_move[0], self.center[1] + self.vec[1] * (self.speed * 2) + map_move[1])
        colizer = pygame.sprite.spritecollideany(self, self.board.collide_group)
        if colizer is not None:
            if pygame.sprite.collide_mask(self, colizer) is not None:
                self.center = self.center[0], backup[1]
                self.point = self.logica()
        self.rect.center = (self.center[0] + map_move[0],
                            self.center[1] + map_move[1])


class Closer(Enemy):
    def __init__(self, spell_group, board):
        super().__init__(spell_group=spell_group, image='Door.png', board=board)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(0, 0))
        self.damage = 10

    def update(self, map_move, player, board):
        self.logica = lambda: (
            randint(*sorted([self.rect.center[0] - int(map_move[0]), player.rect.center[0] - int(map_move[0])])),
            randint(*sorted([self.rect.center[1] - int(map_move[1]), player.rect.center[1] - int(map_move[1])])))
        super().update(map_move=map_move, board=board)


class Ranger(Enemy):
    def __init__(self, spell_group, board):
        super().__init__(image='entity.png', spell_group=spell_group, board=board)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(0, 0))

    def update(self, map_move, player, board):
        if time() - self.cooldown_time >= self.cooldown:
            self.cast(map_move, self.spell_group, normolize_vec(
                (player.rect.center[0] - self.rect.center[0], player.rect.center[1] - self.rect.center[1])), board=board)
            self.cooldown_time = time()
            self.cooldown = self.cooldown_logica()
        super().update(map_move=map_move, board=board)

    def cast(self, map_move, spell_group, vec, board):
        spell_line = [Bolt, Sin]
        spell = spell_line[0](board)
        spell_group.add(spell)
        spell.cast(map_move=map_move, summoner=self, vec=vec, spell_line=spell_line[1:], board=board)
