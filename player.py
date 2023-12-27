import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load('assets/spritegoku.png').convert_alpha()
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface(self.sprite.get_size())
        image.blit(self.sprite, (0, 0), (x, y, image.get_width(), image.get_height()))
        return image

