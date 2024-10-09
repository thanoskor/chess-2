import pygame
from ui import TILE_SIZE

Board = [[None for i in range(8)]for i in range(8)]
all_pieces = []

class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        all_pieces.append(self)
        self.receiving_events = False

    def got_clicked(self):
        self.receiving_events = True

    def get_square(self, mousep):
        return mousep[0]//TILE_SIZE, mousep[1]//TILE_SIZE

    def handle_events(self, event):
        print(event)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = self.get_square(pygame.mouse.get_pos())
            Board[self.row][self.col] = None
            self.row = x
            self.col = y
            Board[x][y] = self
            self.receiving_events = False

class Pawn(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "p"

Pawn(1,1,"w")

for piece in ALL_PIECES:
    Board[piece.row][piece.col] = piece
