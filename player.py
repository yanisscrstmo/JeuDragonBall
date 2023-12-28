import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x ,y,sprite):
        """
        :param x: int, La position en x
        :param y: int, La position en y
        :param sprite: str, Le chemin jusqu'au sprite en png de forme assets/sprites/sprite.png
        """
        super().__init__()
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.position = [x, y]
        self.vitesse = 3
        # self.sprites = {
        #     'normal': self.sprite,
        #     'inversé': self.sprite_inv
        # }

    # def change_direction(self, key, colorkey):
    #     """
    #     :param key: str, La clé du dictionnaire self.sprites
    #     :param colorkey: list , une liste de 3 éléments de la forme [255,255,255] (blanc) qui est le code RGB de la couleur à enlever.
    #     """
    #     self.sprite = self.sprites[key]
    #     self.sprite.set_colorkey(colorkey)

    def move_right(self):
        self.position[0] += self.vitesse

    def move_left(self):
        self.position[0] -= self.vitesse

    def move_up(self):
        self.position[1] += self.vitesse

    def move_down(self):
        self.position[1] -= self.vitesse

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


