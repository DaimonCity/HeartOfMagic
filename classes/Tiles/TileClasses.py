import pygame
from scripts.image_scripts import *


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('test_image.jpg')
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, x, y, board):
        self.image = pygame.transform.scale(self.image, (board.cell_size, board.cell_size))
        self.rect.update(x * board.cell_size + board.left, y * board.cell_size + board.top, board.cell_size,
                         board.cell_size)


class WallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('Wall repeat.png')


class FloorTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('floor.png')


class DoorTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('Door.png')


class UpperLeftCornerTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('UpLeftCor.png')


class DownerLeftCornerTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('DownLeftCor.png')


class UpperRightCornerTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('UpRightCor.png')


class DownerRightCornerTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('DownRightCor.png')


class RightWallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('RightWall.png')


class LeftWallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('LeftWall.png')


class TToUpTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-to-Up.png')


class TToAllTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-to-all.png')


class TToDownTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-to-Down.png')


class TRightWallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-LeftWall.png')


class TLeftWallTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-RightWall.png')


class TLeftWallForRoomTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('T-LeftWallForRoom.png')


class SideDoorTile(Tile):
    def __init__(self):
        super().__init__()
        self.image = load_image('SideDoor.png')
