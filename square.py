ROWS = [0, 1, 2, 3, 4, 5, 6, 7]
COLS = ["a", "b", "c", "d", "e", "f", "g"]
PIECES = ["P", "K", "B", "R", "Q", "K"]

class square:

    def __init__(self, row, col, piece) -> None:
        self.row = row
        self.col = col
        self.piece = piece
    
    def remove_piece(self):
        self.piece = None
    
    def place_piece(self, piece):
        self.piece = piece
