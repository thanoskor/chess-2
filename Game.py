import pygame
import sys
from UI import *
from pieces import *

Board = [[None for i in range(8)]for i in range(8)]

for piece in ALL_PIECES:
    Board[piece.row][piece.col] = piece


ui = UI()
class GAME:
    def __init__(self) -> None:
        pass
    
    def get_square(self, mousep):
        return mousep[0]//TILE_SIZE, mousep[1]//TILE_SIZE

    def start(self): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.get_square(pygame.mouse.get_pos())
                    if Board[x][y]:
                        Board[x][y].got_clicked()
            
            pygame.display.flip()         
            ui.draw_board()
            ui.draw_pieces(ALL_PIECES)
            ui.update()

game = GAME()
game.start()
