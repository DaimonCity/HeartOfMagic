import pygame
from pygame import Color
class RoomBoard:
    def __init__(self, parent):
        self.player_speed = 1
        self.width = 3
        self.color = 0
        self.height = 3
        self.board = [[0] * self.height for _ in range(self.width)]
        self.left = parent.left
        self.top = parent.top
        self.cell_size = parent.cell_size // 3

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, parent_x, parent_y, parent):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 1:
                    r = self.cell_size
                else:
                    r = 1
                if self.color == 0:
                    color = Color('white')
                else:
                    color = Color('green')

                self.true_left = self.left + parent_x * parent.cell_size
                self.true_top = self.top + parent_y * parent.cell_size
                pygame.draw.rect(screen, color, (x * self.cell_size + self.true_left, y * self.cell_size + self.true_top, self.cell_size, self.cell_size), r)
    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.true_left) // self.cell_size, (mouse_pos[1] - self.true_top) // self.cell_size)
        if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
            return pos
        return (0, 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell != None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]] = abs(self.board[cell[0]][cell[1]] - 1)
        print(cell)