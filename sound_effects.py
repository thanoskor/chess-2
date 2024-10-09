import pygame

class sound_mixer:
    def __init__(self) -> None:
        pygame.mixer.init()
        self.capture_sound = pygame.mixer.Sound('chess-2\sound_effects\capture.wav')
    
    def play_caputure_sound(self):
        self.capture_sound.set_volume(1.0)
        self.capture_sound.play()

sounds = sound_mixer()