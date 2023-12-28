import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        super().__init__()
        self.sprite = pygame.image.load('assets/sprites/Goku_11.png')
        self.rect = self.sprite.get_rect()
        self.position = [x, y]

    def update(self):
        self.rect.topleft = self.position

    def resize(self, new_width, new_height, colorkey):
        """
        :param new_width: int, La nouvelle largeur du sprite voulue.
        :param new_height: int, La nouvelle hauteur du sprite voulue.
        :param colorkey: list , une liste de 3 éléments de la forme [255,255,255] (blanc) qui est le code RGB de la couleur à enlever.
        """
        self.image = pygame.transform.scale(self.sprite, (new_width, new_height))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()


