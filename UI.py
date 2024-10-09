import pygame
import sys

size = 800
WIDTH = size
HEIGHT = size
TILE_SIZE = size // 8

DARK_SQUARE_COLOR = (118, 150, 86)
LIGHT_SQUARE_COLOR = (238, 238, 210)
CIRCLE_COLOR = (100, 100, 100)

def get_square(mousep):
    return [mousep[1]//TILE_SIZE, mousep[0]//TILE_SIZE]

class Ui:
    
    def __init__(self, fps) -> None:
        self.main_window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.dot_points = []
        self.frame_rate = fps
        self.clock = pygame.time.Clock()
    
    def update(self):
        pygame.display.flip()
        self.clock.tick(self.frame_rate)
    
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

    def clear_dot_points(self):
        self.dot_points = []

    def draw_dots(self):
        for point in self.dot_points:
            center = (point[1]*TILE_SIZE + TILE_SIZE//2, point[0]*TILE_SIZE + TILE_SIZE//2)
            radius = 10
            pygame.draw.circle(self.main_window, CIRCLE_COLOR, center, radius)

    def draw_pieces(self, pieces):
        for piece in pieces:
            image_path = f"chess-2\piece-sprites\{piece.color}{piece.type}.png"
            image = pygame.image.load(image_path)
            scaled_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            y = piece.row * TILE_SIZE
            x = piece.col * TILE_SIZE
            self.main_window.blit(scaled_image, (x, y))

ui = Ui(60)