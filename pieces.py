import pygame
from Ui import *

Board = [[None for i in range(8)]for i in range(8)]
all_pieces = []

class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        all_pieces.append(self)
        self.receiving_events = False

    def start_receiving_events(self):
        self.receiving_events = True

    def stop_receiving_events(self):
        self.receiving_events = False
    
    def move_self(self, place):
        Board[self.row][self.col] = None
        self.row = place[0]
        self.col = place[1]
        Board[self.row][self.col] = self

class Pawn(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "p"

    def get_legal_moves(self):
        legal_moves = []
        
        if self.color == "w":
            move_up = -1
        else:
            move_up = 1

        if 0 <= self.row + move_up < 8:
            if Board[self.row + move_up][self.col] is None:
                legal_moves.append([self.row + move_up, self.col])

        return legal_moves
    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.stop_receiving_events()
            ui.clear_dot_points()
            potential_move = get_square(pygame.mouse.get_pos())
            if potential_move in self.get_legal_moves():
                self.move_self(potential_move)
        
    def add_legal_moves_to_ui(self):
        legal_moves = self.get_legal_moves()
        if legal_moves:
            ui.add_dot_points(legal_moves)

for i in range(8):
    Pawn(1,i,"b")
    Pawn(6, i, "w")

for piece in all_pieces:
    Board[piece.row][piece.col] = piece
