from pieces import *
from board import *
import pygame
import sys

color_pallet = {"black": (23, 100, 15), "white": (255, 255, 255)}

board = Board(800, 800, color_pallet)
test_sprite = piece(0, 0, "w", "k")
sprite2 = piece(0, 1, "b", "q")

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

    board.draw_board()
    all_sprites.draw(board.window)

    # Update the display
    pygame.display.flip()
