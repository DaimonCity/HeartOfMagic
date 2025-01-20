import copy
import pygame
from copy import *
from pprint import pprint
from classes.Tiles.TileClass import Tile


class Board:
    def __init__(self, map, tiles_dict, parent=0, child=0, left=0, top=0, cell_size=50):
        self.map = map
        self.size = self.width, self.height = len(map[0]), len(map)
        self.tiles_dict = tiles_dict
        self.parent = parent
        self.child = child
        self.sprite_group = pygame.sprite.Group()
        if parent != 0:
            self.left = parent.left
            self.top = parent.top
            self.cell_size = parent.cell_size / self.width
        else:
            self.left = left
            self.top = top
            self.cell_size = cell_size
        if child != 0:
            self.board = [[child for w in range(self.width)] for h in range(self.height)]
        else:
            # self.board = [[self.tiles_dict[map[h][w]] for w in range(self.width)] for h in range(self.height)]
            self.board = []
            for h in range(self.height):
                row = []
                for w in range(self.width):
                    # JVM: Здесь ты в переменную добавляешь копию одного из Tile
                    tile = copy(self.tiles_dict[map[h][w]])
                    # JVM: А потом добавляешь переменную tile в список
                    row.append(copy(tile))

                    # Но пайтон, возможно, меняет результат функции при изменении переменной tile
                    '''Поэтому лучше сделать типа:
                    
                    row.append(copy(self.tiles_dict[map[h][w]])
                    
                    Возможно, оно поможет'''
                self.board.append(row)
            print(self.board[0][0] == self.board[0][1])
            for row in self.board:
                self.sprite_group.add(row)

    def render(self, screen, parent_x=0, parent_y=0, parent=0):
        for y in range(self.height):
            for x in range(self.width):
                self.board[y][x].render(screen, x, y, self)
        self.sprite_group.draw(screen)

        # print(self.sprite_group.sprites())
    # def get_cell(self, mouse_pos):
    #     pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
    #     if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
    #         return pos
    #     return (0, 0)
    #
    # def get_click(self, mouse_pos):
    #     cell = self.get_cell(mouse_pos)
    #     if (cell != None) and (cell[0] >= 0) and (cell[1] >= 0):
    #         self.on_click(cell)
    #         self.board[cell[0]][cell[1]].get_click(mouse_pos)
    # def on_click(self, cell):
    #     pass
