import pygame
import pytmx
import pyscroll
import sqlite3
from pygame.locals import *
from player import Player

base_donnees = sqlite3.connect("game_datas.db")
curseur = base_donnees.cursor()

pygame.mixer.init()
kamehameha = pygame.mixer.Sound("assets/kamehameha-sound-effects-made-with-Voicemod-technology.mp3")

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

class Jeu:
    def __init__(self):
        self.screen = pygame.display.set_mode((1648, 1056))
        pygame.display.set_caption("Dragon Ball FighterGT")

        tmx_data = pytmx.util_pygame.load_pygame("map_assets/map.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_calques = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        self.player = Player()

        self.group = pyscroll.PyscrollGroup(map_layer=map_calques, default_layer=1)
        self.group.add(self.player)




# class Player_infos():
#     def __init__(self, screen, font):
#         self.curseur = curseur
#         self.joueur_1 = joueur_1
#         self.joueur_2 = joueur_2
#         self.rect_p2 = player2_rect
#         self.screen = screen
#         self.font = font
#         self.pv_joueur_1 = 0
#         self.pv_joueur_2 = 0
#         self.att_min_joueur_1 = 0
#         self.att_min_joueur_2 = 0
#         self.att_max_joueur_1 = 0
#         self.att_max_joueur_2 = 0
#
#     def player_health(self):
#         self.pv_joueur_1 = \
#         self.curseur.execute("SELECT PV FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
#         self.pv_joueur_2 = \
#         self.curseur.execute("SELECT PV FROM Stats WHERE NOM LIKE ?", (self.joueur_2,)).fetchone()[0]
#
#     def player_attack(self):
#         self.att_min_joueur_1 = \
#         self.curseur.execute("SELECT ATT_MIN FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
#         self.att_min_joueur_2 = \
#         self.curseur.execute("SELECT ATT_MIN FROM Stats WHERE NOM LIKE ?", (self.joueur_2,)).fetchone()[0]
#         self.att_max_joueur_1 = \
#         self.curseur.execute("SELECT ATT_MAX FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
#         self.att_max_joueur_2 = \
#         self.curseur.execute("SELECT ATT_MAX FROM Stats WHERE NOM LIKE ?", (self.joueur_2,)).fetchone()[0]
#
#     def afficher(self, rect_p2):
#         self.player_health()
#         texte_surface = self.font.render(f"Pv Joueur 2: {str(self.pv_joueur_2)}", True, (255, 255, 255))
#         texte_rect = texte_surface.get_rect(midtop=(self.rect_p2.centerx, self.rect_p2.top - 10))



    def run(self):
        running = True

        self.group.draw(self.screen)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == JOYBUTTONDOWN:
                    if event.button == 0:
                        kamehameha.play()
                        print("Bouton A enfoncé ! Kamehameha!")

        pygame.quit()