import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load('assets/sprites/Goku_11.png').convert_alpha()
        self.image = self.sprite.copy()  # Utilisez une copie pour éviter de modifier l'original
        self.rect = self.image.get_rect()

    def resize(self, new_width, new_height):
        self.image = pygame.transform.scale(self.sprite, (new_width, new_height))
        self.rect = self.image.get_rect()


