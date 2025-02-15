import copy
import pygame
from copy import *
from scripts.image_scripts import load_image


class Board:
    def __init__(self, screen, any_map, tiles_dict, parent=0, child=0, left=0, top=0, cell_size=50):
        self.map = any_map
        self.collide_group = pygame.sprite.Group()
        self.screen = screen
        self.size = self.width, self.height = len(any_map[0]), len(any_map)
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
            self.board = [[child for _ in range(self.width)] for _ in range(self.height)]
        else:
            self.full_up()
        self.do_colission()

    def full_up(self):
        self.board = [[copy(self.tiles_dict[self.map[h][w]]()) for w in range(self.width)] for h in range(self.height)]

    def do_colission(self):
        for i in range(self.height):
            for j in range(self.width):
                if not (self.board[i][j].__class__ in (
                        self.tiles_dict[20], self.tiles_dict[0], self.tiles_dict[2], self.tiles_dict[17])):
                    self.collide_group.add(self.board[i][j])

    def render(self, screen, parent_x=0, parent_y=0, parent=0):
        self.sprite_group = pygame.sprite.Group()
        c = 0
        for y in range(self.height):
            for x in range(self.width):
                c += 1
                self.board[y][x].update(x, y, self)
                self.sprite_group.add(self.board[y][x])
        self.sprite_group.draw(screen)

    def update(self, left=None, top=None):
        if not (None in [left, top]):
            self.left, self.top = left, top

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell is not None) and (cell[0] >= 0) and (cell[1] >= 0):
            return self.on_click(cell)

    @staticmethod
    def on_click(cell):
        return cell

    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if 0 <= pos[0] <= self.width - 1 and 0 <= pos[1] <= self.height - 1:
            return pos
        return None


class UI(Board):
    def __init__(self, screen, any_map, tiles_dict, parent=0, child=0, left=0, top=0, cell_size=50):
        super().__init__(screen, any_map, tiles_dict, parent, child, left, top, cell_size)

    def do_colission(self):
        pass

    def full_up(self):
        self.board = [[copy(self.tiles_dict[self.map[h][w]](self)) for w in range(self.width)] for h in
                      range(self.height)]

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                self.screen.blit(pygame.transform.scale(load_image('Empty_slot.png'), (32 * 3, 32 * 3)),
                                 (self.board[y][x].rect.x + x * self.cell_size + self.left,
                                  self.board[y][x].rect.y + y * self.cell_size + self.top,
                                  *self.board[y][x].rect.size))
                self.screen.blit(self.board[y][x].logo, (self.board[y][x].rect.x + x * self.cell_size + self.left,
                                                         self.board[y][x].rect.y + y * self.cell_size + self.top,
                                                         *self.board[y][x].rect.size))
        self.sprite_group.draw(self.screen)
