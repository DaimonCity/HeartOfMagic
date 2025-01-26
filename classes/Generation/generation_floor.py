import pygame
import random
from pprint import pprint

# SEED = "9 1 2 0 3 9 2 1 0 9 4 1 2"

# Пусто поле
EMPTY_MAP = [[4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
             [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7]]

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
        #     xy1, xy2 = xy2, xy1
        # print("res=", xy1, xy2, "check=", (0 > xy1 and xy2 > 15 or 0 > xy2 and xy1 > 15))
        # if not((0 > xy1 and xy2 > 15) or (0 > xy2 and xy1 > 15)):
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
            while self.map[y][x] == 0:
                self.map[y][x] = 1
                if direct == 'right':
                    x += 1
                else:
                    x -= 1
            self.set_next_object(y, x, 'x')
            x0 = choice_cord(start_x, x)
            if x0 is False:
                return
            self.map[y][x0] = 9
            self.draw_line((x0, y - 1), 'y', 'top')
            x1 = choice_cord(start_x, x)
            if x1 == x0:
                self.map[y][x0] = 12
            else:
                self.map[y][x1] = 13
            self.draw_line((x1, y + 1), 'y', 'bottom')
        else:  # axis == 'y'
            while self.map[y][x] == 0:
                self.map[y][x] = 8
                if direct == 'top':
                    y -= 1
                else:
                    y += 1
            self.set_next_object(y, x, 'y', direct)
            y0 = choice_cord(start_y, y)
            if y0 is False:
                return
            self.draw_line((x + 1, y0), 'x', 'right')
            y1 = choice_cord(start_y, y)
            self.draw_line((x - 1, y1), 'x', 'left')
            if y1 == y0:
                self.map[y0][x] = 12
            else:
                self.map[y0][x] = 14
                self.map[y1][x] = 16

    def put_in_doors(self):
        for cord_y in range(1, 15):
            for cord_x in range(1, 15):
                if self.map[cord_y][cord_x] == 1:
                    if ((self.map[cord_y - 1][cord_x] == 1 or self.map[cord_y + 1][cord_x] == 1)
                            and self.map[cord_y][cord_x + 1] != 1):
                        continue
                    else:
                        x0 = cord_x
                        x1 = len(self.map[cord_y]) - 2
                        for one in range(1, 15):
                            if self.map[cord_y][cord_x] == 1:
                                if self.map[cord_y - 1][cord_x] == 1 or self.map[cord_y + 1][cord_x] == 1:
                                    x1 = one - 1

                        self.map[cord_y][random.randint(x0, x1 - 1)] = 2
                        break

    def set_next_object(self, cord_y, cord_x, axis, direct=''):
        if axis == 'x':
            _object = self.map[cord_y][cord_x]
            if _object == 11:
                self.map[cord_y][cord_x] = 15
            # if _object == 8:
            #     self.map[cord_y][cord_x] = 14
        else:  # axis == 'y'
            _object = self.map[cord_y][cord_x]
            if _object == 1 and direct == 'bottom':
                self.map[cord_y][cord_x] = 9
            elif _object == 1:
                self.map[cord_y][cord_x] = 13
            elif _object == 13:
                self.map[cord_y][cord_x] = 12

    def set_one_sprite(self, _x, _y, num):
        self.map[_y][_x] = num

    def get_map(self):
        return self.map

# Тесты класса
# game = Map(EMPTY_MAP)
# print()
# seed = '9594'
# direction = True
# _y = choice_cord(1, len(game.map) - 1)
# game.draw_line((1, _y), 'x', 'right')
# pprint(game.get_map())
# game.put_in_doors()
# pprint(game.get_map())
