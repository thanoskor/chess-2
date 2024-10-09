ALL_PIECES = []

class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        ALL_PIECES.append(self)

    def got_clicked(self):
        print("!!")

class Pawn(Piece):
    def __init__(self, row, col, color) -> None:
        super().__init__(row, col, color)
        self.type = "p"

Pawn(1,1,"w")