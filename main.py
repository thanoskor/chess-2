import pprint as p
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Board')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw the chessboard
def draw_board():
    tile_size = WIDTH // 8  # Each tile size

    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(window, color, (col * tile_size, row * tile_size, tile_size, tile_size))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw the chessboard
    draw_board()
    
    # Update the display
    pygame.display.flip()
