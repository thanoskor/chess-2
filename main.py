import pygame
import sys
from Ui import *
from pieces import *

class Game:
    def __init__(self) -> None:
        self.to_move = "w"
    
    def is_a_king_in_check(self):
        kings = []

        for piece in all_pieces:
            if piece.type == "k":
                kings.append(piece)

        for king in kings:
            for enemy_piece in all_pieces:
                if enemy_piece.color != king.color:
                    for move in enemy_piece.legal_moves:
                        if move[0] == king.row and move[1] == king.col:
                            return True
        return False

    def alternate_player(self):
        if self.to_move == "w":
            self.to_move = "b"
        else:
            self.to_move = "w"

    def start(self): 
        selected_piece = None
        self.to_move = "w"
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if selected_piece:
                    feedback = selected_piece.await_for_command(event)
                    if feedback == "unselected":
                        selected_piece = None
                    elif feedback == "moved":
                        selected_piece = None
                        self.alternate_player()
                        break
                    else:
                        pass
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = get_mouse_rc()
                    if Board[row][col]:
                        if Board[row][col].color == self.to_move:
                            selected_piece = Board[row][col]
                            Board[row][col].got_selected()

            ui.draw_board()
            ui.draw_pieces(all_pieces)
            ui.draw_move_indicator_dots()
            ui.update()

game = Game()
game.start()
