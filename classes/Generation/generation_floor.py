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
                print("cords:", x, y)

            x0 = choice_cord(start_x, x)
            print("point:", x0)
            x1 = choice_cord(x0, x)
            print("point:", x1)

            #  ##########################################################
            cords = self.cords_for_door(direct, y, start_x, x0, axis, x)
            #  ###########################################################

            if cords is None or cords is False:
                return
            self.set_door(cords, axis)

            self.map[y][x0] = 9
            self.draw_line((x0, y - 1), 'y', 'top')

            #  ##########################################################
            cords = self.cords_for_door(direct, y, start_x, x1, axis, x)
            #  ###########################################################

            if cords is None or cords is False:
                return
            self.set_door(cords, axis)

            if x1 == x0:
                self.map[y][x0] = 12
            else:
                self.map[y][x1] = 13

            self.set_next_object(y, x, axis, direct)

            self.draw_line((x1, y + 1), 'y', 'bottom')

        else:  # axis == 'y'
            while self.map[y][x] == 0:
                self.map[y][x] = 8
                if direct == 'top':
                    y -= 1
                else:
                    y += 1
                print("cords:", x, y)

            y0 = choice_cord(start_y, y)
            print("point:", y0)
            y1 = choice_cord(start_y, y)
            print("point:", y1)

            cords = self.cords_for_door(direct, x, start_y, y0, axis, y)
            if cords is None or cords is False:
                self.set_next_object(y, x, 'y', direct)
                return
            self.set_door(cords, axis)

            self.map[y0][x] = 14
            self.draw_line((x + 1, y0), 'x', 'right')

            cords = self.cords_for_door(direct, x, start_y, y1, axis, y)
            if cords is None or cords is False:
                self.set_next_object(y, x, 'y', direct)
                return

            if y1 == y0:
                self.map[y1][x] = 12
            else:
                self.map[y1][x] = 16

            self.set_next_object(y, x, 'y', direct)

            self.set_door(cords, axis)
            self.draw_line((x - 1, y1), 'x', 'left')

    def set_next_object(self, cord_y, cord_x, axis, direct=''):
        _object = self.map[cord_y][cord_x]
        if axis == 'x':

            if direct == 'right':
                if _object == 11:
                    self.map[cord_y][cord_x] = 15
                elif _object == 8 and cord_y != 15:
                    self.map[cord_y][cord_x] = 16

            elif direct == 'left':
                if _object == 8:
                    self.map[cord_y][cord_x] = 14
                elif _object == 8 and cord_y != 0:
                    self.map[cord_y][cord_x] = 14

        else:  # axis == 'y'

            if direct == 'top':
                if _object == 1:
                    self.map[cord_y][cord_x] = 13
                elif _object == 2:
                    self.map[cord_y][cord_x] = 13
                elif _object == 13:
                    self.map[cord_y][cord_x] = 12
                elif _object == 9:
                    self.map[cord_y][cord_x] = 1

            elif direct == 'bottom':
                if _object == 1:
                    self.map[cord_y][cord_x] = 9
                elif _object == 13:
                    self.map[cord_y][cord_x] = 12
                elif _object == 2:
                    self.map[cord_y][cord_x] = 9

    def set_one_sprite(self, _x, _y, num):
        self.map[_y][_x] = num

    def set_door(self, cords, axis):
        list_1 = cords
        print("All cords:", cords)

        for cord in cords:
            if self.map[cord[0]][cord[1]] != 1 or self.map[cord[0]][cord[1]] != 8:
                list_1.remove(cord)

        print("Available cords: ", list_1)
        door = random.choice(list_1)
        print("Chosen door: ", door)
        if axis == 'x':
            self.map[door[0]][door[1]] = 2
        else:  # axis == 'y'
            self.map[door[0]][door[1]] = 17

    def cords_for_door(self, direct, const, start_point, finish_point, axis, last_point):
        if finish_point is False:
            if direct == "top":
                cords = [(cord_y, const) for cord_y in range(last_point, start_point)]
            elif direct == 'left':
                cords = [(const, cord_x) for cord_x in range(last_point, start_point)]

            elif direct == 'right':
                cords = [(const, cord_x) for cord_x in range(start_point, last_point)]
            else:  # direct == "bottom"
                cords = [(cord_y, const) for cord_y in range(start_point, last_point)]
            self.set_door(cords, axis)
            return

        elif direct == "top":
            cords = [(cord_y, const) for cord_y in range(finish_point, start_point)]
        elif direct == 'left':
            cords = [(const, cord_x) for cord_x in range(finish_point, start_point)]
        elif direct == 'right':
            cords = [(const, cord_x) for cord_x in range(start_point, finish_point)]
        else:  # direct == "bottom"
            cords = [(cord_y, const) for cord_y in range(start_point, finish_point)]
        return cords

    def get_map(self):
        return self.map

# # Тесты класса
# game = Map(EMPTY_MAP)
# print()
# _y = choice_cord(1, len(game.map) - 1)
# game.draw_line((1, _y), 'x', 'right')
# pprint(game.get_map())
