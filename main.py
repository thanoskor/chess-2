from pieces import *
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
all_sprites = pygame.sprite.Group()

test_sprite = piece(0, 0, "w", "k")

all_sprites.add(test_sprite)

# Main loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_mouse_position = pygame.mouse.get_pos()
            curret_square = get_square(current_mouse_position)
            for sprite in all_sprites:
                if sprite.return_square_pos() == curret_square:
                    sprite.got_clicked()

    draw_board()
    all_sprites.draw(window)

    # Update the display
    pygame.display.flip()
