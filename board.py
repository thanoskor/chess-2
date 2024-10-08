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

    def fill_board_with_square_objects(self):
        pass
    
    def draw_board(self):
        # Each tile size
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.color_pallet["white"]
                else:
                    color = self.color_pallet["black"]
                pygame.draw.rect(self.window, color, (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
