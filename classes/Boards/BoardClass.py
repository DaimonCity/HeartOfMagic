import copy
import pygame
from copy import *
from pprint import pprint
from classes.Tiles.TileClasses import Tile


class Board:
    def __init__(self, screen, map, tiles_dict, parent=0, child=0, left=0, top=0, cell_size=50):
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
        self.cons_cell_size = self.cell_size
        if child != 0:
            self.board = [[child for w in range(self.width)] for h in range(self.height)]
        else:
            self.board = [[copy(self.tiles_dict[map[h][w]]) for w in range(self.width)] for h in range(self.height)]
    def render(self, screen, parent_x=0, parent_y=0, parent=0):
        for y in range(self.height):
            for x in range(self.width):
                self.board[y][x].render(x, y, self)
                screen.blit(self.board[y][x].image, self.board[y][x].rect)
        self.sprite_group.draw(screen)
    def update(self, left=None, top=None, zoom=None):
        if not(left == top == None):
            self.left, self.top = left, top
        if zoom != None:
            self.cell_size = self.cons_cell_size * zoom


