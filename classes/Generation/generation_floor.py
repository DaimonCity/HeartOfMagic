import pygame
import random
from pprint import pprint

# SEED = "9 1 2 0 3 9 2 1 0 9 4 1 2"

# Пусто поле
EMPTY_MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Объекты на карте
objects = {0: "floor",
           1: "wall",
           2: "door"}


# # Мои тесты
# pprint(EMPTY_MAP)
# print()
# EMPTY_MAP[0][1] = 1
# pprint(EMPTY_MAP)


# Класс для создания (генерации) карты


def choice_cord(xy1, xy2):
    if xy1 > xy2:
        xy1, xy2 = xy2, xy1
    xy1, xy2 = xy1 + 4, xy2 - 4
    if xy1 == xy2:
        return xy1

    if xy1 > xy2:
        return False
    return random.randint(xy1, xy2)


class Map:
    def __init__(self, list_map):
        self.map = list_map
        self.w, self.h = self.size = len(list_map[0]), len(list_map)

    def make_board(self):
        for y in range(self.h):
            for x in range(self.w):
                if x == 0 or y == 0 or x == self.w - 1 or y == self.h - 1:
                    self.map[y][x] = 1
        return self.map

    def draw_line(self, consts, axis, direct):
        if consts is False:
            return
        start_x, start_y = consts
        x = start_x
        y = start_y
        if axis == 'x':
            while self.map[y][x] != 1:
                self.map[y][x] = 1
                if direct == 'right':
                    x += 1
                else:
                    x -= 1
            x0 = choice_cord(start_x, x)
            if x0 is False:
                return
            self.draw_line((x0, y - 1), 'y', 'top')
            x0 = choice_cord(start_x, x)
            self.draw_line((x0, y + 1), 'y', 'bottom')
        else:  # axis == 'y'
            while self.map[y][x] != 1:
                self.map[y][x] = 1
                if direct == 'top':
                    y -= 1
                else:
                    y += 1
            y0 = choice_cord(start_y, y)
            if y0 is False:
                return
            self.draw_line((x + 1, y0), 'x', 'right')
            y0 = choice_cord(start_y, y)
            self.draw_line((x - 1, y0), 'x', 'left')

    def get_map(self):
        return self.map


# Тесты класса
game = Map(EMPTY_MAP)
pprint(game.make_board())
print()
seed = '9594'
direction = True
y = choice_cord(1, len(game.map) - 1)
game.draw_line((1, y), 'x', 'right')
pprint(game.get_map())
