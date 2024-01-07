import pygame

from game import Jeu
from welcome import *

if __name__ == '__main__':
    pygame.init()
    game = Jeu()
    welcome = Accueil()
    welcome.run()
    game.run()