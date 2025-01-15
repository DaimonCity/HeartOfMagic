import pygame
from pygame import Color
from RoomBoard import RoomBoard
class Board:
    # создание поля
    def __init__(self, width=5, height=5, left=20, top=50, cell_size=200, BabyBoard=0, parent=0):
        self.width = width
        self.height = height
        self.color = 0
        self.left = left
        self.top = top
        self.parent = parent
        self.cell_size = cell_size
        self.BabyBoard = BabyBoard
        self.board = [[BabyBoard for i in range(height)] for _ in range(width)]

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render_tile(self, screen, x, y):
        if self.board[x][y] == 1:
            r = self.cell_size
        else:
            r = 1
        if self.color == 0:
            color = Color('white')
        else:
            color = Color('green')
        pygame.draw.rect(screen, color, (x * self.cell_size + self.true_left, y * self.cell_size + self.true_top, self.cell_size, self.cell_size), r)

    def render(self, screen, parent_x=0, parent_y=0):
        if self.parent != 0:
            self.true_left = self.left + parent_x * self.parent.cell_size
            self.true_top = self.top + parent_y * self.parent.cell_size
        for y in range(self.height):
            for x in range(self.width):
                if self.BabyBoard != 0:
                    self.board[x][y].render(screen, x , y, self)
                else:
                    self.render_tile(screen, x, y)

    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.true_left) // self.cell_size, (mouse_pos[1] - self.true_top) // self.cell_size)
        if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
            return pos
        return (0, 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell != None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)
            self.board[cell[0]][cell[1]].get_click(mouse_pos)

    def on_click(self, cell):
        pass
