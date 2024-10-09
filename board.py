import pygame
from pieces import *
from square import *

class Board:

    def __init__(self, width, height, color_pallet):
        self.color_pallet = color_pallet
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))    
        pygame.display.set_caption('Chess')
        self.tile_size = self.width // 8
        self.grid = []
        self.fill_board_with_square_objects()
    
    def fill_board_with_square_objects(self):
        for row in range(8):
            self.grid.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.color_pallet["white"]
                else:
                    color = self.color_pallet["black"]
                self.grid[row].append(square(row, col, self.tile_size, color))

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                self.grid[row][col].draw_self(self.window)

