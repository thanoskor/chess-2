import pygame
import sys
import UI

ui = UI.UI()
class GAME:
    def __init__(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()         
            ui.draw_board()
            points = []   #[[1, 1], [1, 0], [0, 1]]
            ui.add_dot_points(points)
            ui.draw_dots()
            ui.update()

game = GAME()