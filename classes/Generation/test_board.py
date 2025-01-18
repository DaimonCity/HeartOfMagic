import pygame
from pygame import Color


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
        self.board = [[0] for _ in range(width)]

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, s):
        for y in range(0, self.height):
            for x in range(0, self.width):
                pygame.draw.rect(s, Color("White"), (
                x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                self.cell_size), 1)

    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
            return pos
        return (0, 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell is not None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)
            self.board[cell[0]][cell[1]].get_click(mouse_pos)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]].color = abs(self.board[cell[0]][cell[1]].color - 1)


if __name__ == '__main__':
    pygame.init()

    size = w, h = 800, 600
    screen = pygame.display.set_mode(size)

    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
