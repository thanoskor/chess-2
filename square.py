import pygame

class piece(pygame.sprite.Sprite):

    def __init__(self, image_path, position, color):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

class pawn(piece):
    
    def __init__(self, position):
        super().__init__("test_sprite.png", position)
