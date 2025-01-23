import pygame
from pygame import Color
from RoomBoard import RoomBoard


class Board:
    # создание поля
    def __init__(self, width, height):
        self.player_speed = 1
        self.width = width
        self.height = height
        self.color = 0
        self.left = 20
        self.top = 50
        self.cell_size = 200
        self.board = [[RoomBoard(self) for i in range(height)] for _ in range(width)]

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                self.board[x][y].render(screen, x, y, self)

    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
            return pos
        return 0, 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell is not None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)
            self.board[cell[0]][cell[1]].get_click(mouse_pos)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]].color = abs(self.board[cell[0]][cell[1]].color - 1)
