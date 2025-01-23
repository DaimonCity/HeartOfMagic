from classes.Entities.EntityClass import Entity
import pygame
class Freeplace(Entity):
    def __init__(self, screen, vec, player):
        super().__init__()
        self.image = None
        self.rect.update(screen.get_width() / 3 - vec[0] * player.speed, screen.get_height() / 3 - vec[1] ,
                                                screen.get_width() - screen.get_width() / 3 * 2 - vec[0] * player.speed,
                                                screen.get_height() - screen.get_height() / 3 * 2 - vec[1] * player.speed)