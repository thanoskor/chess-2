import pygame
from pieces import *

class square:

    def __init__(self, row, col, tile_size, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.tile_size = tile_size
        self.occupied = False
        self.add_dot = False

    def draw_self(self, window):
        if self.add_dot == False:
            pygame.draw.rect(window, self.color, (self.col * self.tile_size, self.row * self.tile_size, self.tile_size, self.tile_size))
        else:
            pygame.draw.rect(window, self.color, (self.col * self.tile_size, self.row * self.tile_size, self.tile_size, self.tile_size))
            pygame.draw.circle(window, (100,100,100), (self.col*self.tile_size + 50, self.row*self.tile_size + 50), 10)