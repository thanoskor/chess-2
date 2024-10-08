from pieces import *
import pygame
import sys

# Function to draw the chessboard

test_sprite = piece(0, 0, "w", "k")

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
