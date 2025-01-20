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
def random_cord(start_zero, fin_zero):
    rand_cord = random.randint(start_zero, fin_zero)
    while rand_cord < 4 or rand_cord > 11:
        rand_cord = random.randint(start_zero, fin_zero)
    return rand_cord


# def make_seed(_len=6):
#     _seed = []
#     cnt = 0
#     while cnt != _len // 2:
#         start_seed = []
#         for _ in range(2):
#             _num1 = random_cord(4, 11)
#             start_seed.append(_num1)
#
#         for elem in start_seed:
#             _seed.append(elem)
#
#         for elem in start_seed:
#             if random.random():
#                 if elem - 3 > 4:
#                     _num = random_cord(0, elem - 3)
#                 else:
#                     _num = random_cord(elem + 4, 16)
#             else:
#                 _num = random_cord(elem + 4, 16)
#             _seed.append(_num)
#         cnt += 1
#
#     return _seed[:-1]


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

    def draw_line(self, init_x, init_y, direct, count=0):
        if direct == 0:
            for x in range(init_x, 14 + 1):
                self.map[init_y][x] = 1
        else:
            for x in range(init_x, 14 + 1):
                self.map[x][init_y] = 1
        # while count != 2:
        #     count += 1
        #     direction = 1 if direction == 0 else 0
        #     if random.random():
        #         cord = random_cord(init_x + 4, 11)
        #     else:
        #         cord = random_cord(init_x - 4, 4)
        #     self.draw_line(0, cord, direction, count)
        return self.map

    def choice_cords(self):
        pass

    def get_map(self):
        return self.map


# Тесты класса
# game = Map(EMPTY_MAP)
# pprint(game.make_board())
# print()
# seed = make_seed(3)
# direction = 0
#
# for num in seed:
#     game.draw_line(0, int(num), direction)
#     direction = 1 if direction == 0 else 0
# pprint(game.get_map())
