import pygame
import sys

size = 800
WIDTH = size
HEIGHT = size
TILE_SIZE = size // 8

DARK_SQUARE_COLOR = (118, 150, 86)
LIGHT_SQUARE_COLOR = (238, 238, 210)
CIRCLE_COLOR = (100, 100, 100)

class Ui:
    
    def __init__(self) -> None:
        self.main_window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.dot_points = []
        self.all_sprites = pygame.sprite.Group()
    
    def update(self):
        pygame.display.flip()
    
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col)%2 == 0:
                    color = LIGHT_SQUARE_COLOR
                else:
                    color = DARK_SQUARE_COLOR
                rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.main_window, color, rect)

    def add_dot_points(self, points):
        self.dot_points += points

    def draw_dots(self):
        for point in self.dot_points:
            center = (point[0]*TILE_SIZE + TILE_SIZE//2, point[1]*TILE_SIZE + TILE_SIZE//2)
            radius = 10
            pygame.draw.circle(self.main_window, CIRCLE_COLOR, center, radius)

    def draw_pieces(self, pieces):
        for piece in pieces:
            image_path = f"piece-sprites\{piece.color}{piece.type}.png"
            image = pygame.image.load(image_path)
            scaled_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            x = piece.row * TILE_SIZE
            y = piece.col * TILE_SIZE
            self.main_window.blit(scaled_image, (x, y))