import pygame
import sys
from Ui import *
from pieces import *

class Game:
    def __init__(self) -> None:
        pass

    def get_square(self, mousep):
        return mousep[1]//TILE_SIZE, mousep[0]//TILE_SIZE

    def start(self): 
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for piece in all_pieces:
                    if piece.receiving_events:
                        piece.handle_events(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = get_square(pygame.mouse.get_pos())
                    if Board[row][col]:
                        Board[row][col].add_legal_moves_to_ui()
                        Board[row][col].start_receiving_events()
            
            ui.draw_board()
            ui.draw_pieces(all_pieces)
            ui.draw_dots()
            ui.update()

game = Game()
game.start()
