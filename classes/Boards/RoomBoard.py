import pygame
from pygame import Color

class RoomBoard:
    def init(self, parent, parent_x, parent_y):
        # ... (остальной код без изменений)
        self.player_speed = 1
        self.width = 3
        self.color = 0
        self.height = 3
        self.board = [[0] * self.height for _ in range(self.width)]
        self.parent = parent
        self.left = parent.left + parent_x * parent.cell_size
        self.top = parent.top + parent_y * parent.cell_size
        self.cell_size = parent.cell_size // 3

        self.true_left = int()
        self.true_top = int()


    def render(self, screen, parent_x, parent_y, parent):
        for y in range(self.height):
            for x in range(self.width):
                self.true_left = self.left
                self.true_top = self.top
                pygame.draw.rect(screen, color, ( # Рисуем на переданном screen
                    x * self.cell_size + self.true_left, y * self.cell_size + self.true_top, self.cell_size,
                    self.cell_size),
                                 r)