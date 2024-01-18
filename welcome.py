import pygame
# import sys
import random
from game import *

class Accueil():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/dan-dan-kokoro-hikareteku-Good-songz.mp3")
        self.troll = pygame.mixer.Sound("assets/musica_1.wav")
        self.start_sound = pygame.mixer.Sound("assets/kamehameha.swf.mp3")
        pygame.mixer.music.play()

        self.largeur, self.hauteur = 1600, 900
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Dragon Ball Fighter")

        self.fond_accueil = pygame.image.load("assets/téléchargé.png")
        self.image_error = pygame.image.load("assets/Hard-Drive-Error.png").convert_alpha()

        self.police = pygame.font.Font("assets/Saiyan-Sans.ttf", 90)
        self.texte_accueil = self.police.render("Dragon Ball Fighter X", True, (0, 0, 0))

        self.couleur_bouton = (128, 128, 128)
        self.rect_bouton = pygame.Rect(190, 397, 475, 80)

        self.x = (self.largeur - self.image_error.get_width()) // 2
        self.y = (self.hauteur - self.image_error.get_height()) // 2



    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rect_bouton.collidepoint(event.pos):
                            # self.troll.play()
                            pygame.mixer.music.stop()
                            # for i in range(1, 20):
                            #     self.ecran.blit(self.image_error, (random.randint(1, 1100), random.randint(1, 800)))
                            #     pygame.display.flip()
                            #     pygame.time.delay(500)
                            # pygame.time.wait(int(self.troll.get_length() * 650))
                            running = False
                            if not running:
                                self.game = Jeu()
                                self.game.run()

            self.ecran.blit(self.fond_accueil, (0, 0))
            self.ecran.blit(self.texte_accueil, (100, 100))

            pygame.draw.rect(self.ecran, self.couleur_bouton, self.rect_bouton, border_radius=10)

            texte_bouton = self.police.render("Lancer le jeu", True, (0, 0, 0))
            self.ecran.blit(texte_bouton, (200, 400))

            pygame.display.flip()

        pygame.quit()

