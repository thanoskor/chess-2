import pygame
from Ui import *
from sound_effects import *

Board = [[None for i in range(8)]for i in range(8)]
all_pieces = []

class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        all_pieces.append(self)
        self.legal_moves = []
        self.update_legal_moves()
    
    def update_legal_moves(self):
        self.legal_moves = self.get_legal_moves()

    def get_legal_moves(self):
        pass

    def got_selected(self):
        ui.add_move_indicator_dots(self.legal_moves)
    
    def move_self(self, place):
        Board[self.row][self.col] = None
        self.row, self.col = place[0], place[1]
        try:
            all_pieces.remove(Board[self.row][self.col])
            sounds.play_caputure_sound()
        except:
            pass
        Board[self.row][self.col] = self
        
        for piece in all_pieces:
            piece.update_legal_moves()

    def await_for_command(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            ui.clear_move_indicator_dots()
            mouse_cords = get_mouse_rc()
            if mouse_cords in self.legal_moves:
                self.move_self(mouse_cords)
                self.legal_moves = self.get_legal_moves()
                return "moved"
            return "unselected"
        return "no_action"

class Pawn(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "p"
        self.first_move = True

    def get_legal_moves(self):
        legal_moves = []
        
        # Determine direction based on color
        if self.color == "w":
            move_up = -1
            starting_row = 6  # White pawns start from row 6 (2nd rank)
        else:
            move_up = 1
            starting_row = 1  # Black pawns start from row 1 (7th rank)
        
        # Normal one-square move
        if 0 <= self.row + move_up < 8 and Board[self.row + move_up][self.col] is None:
            legal_moves.append([self.row + move_up, self.col])

            # Double move on first move
            if self.row == starting_row and Board[self.row + (2 * move_up)][self.col] is None:
                legal_moves.append([self.row + (2 * move_up), self.col])
        
        # Diagonal captures
        for move_side in [-1, 1]:  # Check left and right diagonals
            new_col = self.col + move_side
            if 0 <= new_col < 8 and 0 <= self.row + move_up < 8:
                target_piece = Board[self.row + move_up][new_col]
                if target_piece is not None and target_piece.color != self.color:
                    legal_moves.append([self.row + move_up, new_col])

        return legal_moves

class Rook(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "r"

    def get_legal_moves(self):
        legal_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

        for direction in directions:
            for step in range(1, 8):  # Can move up to 7 squares
                new_row = self.row + direction[0] * step
                new_col = self.col + direction[1] * step
                
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if Board[new_row][new_col] is None:
                        legal_moves.append([new_row, new_col])
                    elif Board[new_row][new_col].color != self.color:
                        legal_moves.append([new_row, new_col])  # Capture
                        break  # Stop after capturing
                    else:
                        break  # Blocked by own piece
                else:
                    break  # Out of bounds

        return legal_moves

class Knight(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "n"

    def get_legal_moves(self):
        legal_moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for move in knight_moves:
            new_row = self.row + move[0]
            new_col = self.col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = Board[new_row][new_col]
                if target_piece is None or target_piece.color != self.color:
                    legal_moves.append([new_row, new_col])

        return legal_moves

class Queen(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "q"

    def get_legal_moves(self):
        legal_moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Rook moves
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Bishop moves
        ]

        for direction in directions:
            for step in range(1, 8):  # Can move up to 7 squares
                new_row = self.row + direction[0] * step
                new_col = self.col + direction[1] * step
                
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if Board[new_row][new_col] is None:
                        legal_moves.append([new_row, new_col])
                    elif Board[new_row][new_col].color != self.color:
                        legal_moves.append([new_row, new_col])  # Capture
                        break  # Stop after capturing
                    else:
                        break  # Blocked by own piece
                else:
                    break  # Out of bounds

        return legal_moves

class King(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "k"

    def get_legal_moves(self):
        legal_moves = []
        king_moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertical and horizontal
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]

        for move in king_moves:
            new_row = self.row + move[0]
            new_col = self.col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = Board[new_row][new_col]
                if target_piece is None or target_piece.color != self.color:
                    legal_moves.append([new_row, new_col])

        return legal_moves

class Bishop(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "b"

    def get_legal_moves(self):
        legal_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal directions

        for direction in directions:
            for step in range(1, 8):  # Can move up to 7 squares
                new_row = self.row + direction[0] * step
                new_col = self.col + direction[1] * step

                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if Board[new_row][new_col] is None:
                        legal_moves.append([new_row, new_col])
                    elif Board[new_row][new_col].color != self.color:
                        legal_moves.append([new_row, new_col])  # Capture
                        break  # Stop after capturing
                    else:
                        break  # Blocked by own piece
                else:
                    break  # Out of bounds

        return legal_moves

def setup_pieces():
    # Pawns
    for i in range(8):
        Pawn(1, i, "b")
        Pawn(6, i, "w")
    
    # Rooks
    Rook(0, 0, "b")
    Rook(0, 7, "b")
    Rook(7, 0, "w")
    Rook(7, 7, "w")
    
    # Knights
    Knight(0, 1, "b")
    Knight(0, 6, "b")
    Knight(7, 1, "w")
    Knight(7, 6, "w")
    
    # Bishops
    Bishop(0, 2, "b")
    Bishop(0, 5, "b")
    Bishop(7, 2, "w")
    Bishop(7, 5, "w")
    
    # Queens
    Queen(0, 3, "b")
    Queen(7, 3, "w")
    
    # Kings
    King(0, 4, "b")
    King(7, 4, "w")

setup_pieces()

# Updating the board with pieces
for piece in all_pieces:
    piece.update_legal_moves()
    Board[piece.row][piece.col] = piece
