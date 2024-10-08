import pygame
from pieces import *
from square import *

#black and white
#color_pallet = {black: (0, 0, 0), white: (255, 255, 255)}

class Board:
    def __init__(self, width, height, color_pallet):
        self.color_pallet = color_pallet

        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))    
        pygame.display.set_caption('Chess')
        self.tile_size = self.width // 8

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
                pygame.draw.rect(window, color, (col * tile_size, row * tile_size, tile_size, tile_size))
