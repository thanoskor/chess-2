import pygame

def get_checker_cords(row, col):
    tile_size = 800 // 8
    return (row * tile_size, col * tile_size)

def get_square(mouse_pos):
    return (int(mouse_pos[0]//100), int(mouse_pos[1]//100))

class piece(pygame.sprite.Sprite):

    def __init__(self, row, col, color, piece_type):
        image_path = f"chess-2\svgtopng\{color}{piece_type}.png"
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = get_checker_cords(row, col)

    def got_clicked(self):
        self.rect.topleft = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pass
    
    def return_square_pos(self):
        return get_square(self.rect.topleft)

"""
class pawn(piece):
    
    def __init__(self, position):
        super().__init__("test_sprite.png")
"""
