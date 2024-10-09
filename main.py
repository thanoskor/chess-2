import pygame
import sys
from ui import *
from pieces import *

ui = Ui()
class Game:
    def __init__(self, fps) -> None:
        self.frame_rate = fps
        self.clock = pygame.time.Clock()

    def get_square(self, mousep):
        return mousep[0]//TILE_SIZE, mousep[1]//TILE_SIZE

    def start(self): 
        event_receiving_pieces = []
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.get_square(pygame.mouse.get_pos())
                    if Board[x][y]:
                        Board[x][y].got_clicked()
                        event_receiving_pieces.append(Board[x][y])
                
                for piece in event_receiving_pieces:
                    piece.handle_events(event)
            
            for piece in event_receiving_pieces:
                if piece.receiving_events == False:
                    event_receiving_pieces.remove(piece)
        
            ui.draw_board()
            ui.draw_pieces(all_pieces)
            ui.update()
            self.clock.tick(self.frame_rate)

game = Game(60)
game.start()
