import pygame
from pieces import *

class square:

    def __init__(self, row, col, tile_size, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.tile_size = tile_size
        self.occupied = False
        
    def draw_self(self, window):
        pygame.draw.rect(window, self.color, (self.col * self.tile_size, self.row * self.tile_size, self.tile_size, self.tile_size))
    