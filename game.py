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



class Jeu:
    def __init__(self):
        self.screen = pygame.display.set_mode((1648, 1056))
        pygame.display.set_caption("Dragon Ball FighterGT")

        tmx_data = pytmx.util_pygame.load_pygame("map_assets/map.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_calques = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_calques.zoom = 2

        player_position = tmx_data.get_object_by_name("Joueur")
        self.player = Player(player_position.x,player_position.y)
        self.player.resize(49,72,[255,255,255])

        self.group = pyscroll.PyscrollGroup(map_layer=map_calques, default_layer=3)

        self.group.add(self.player)

        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def recup_input_clavier(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            print("haut")
        elif pressed[pygame.K_DOWN]:
            print("bas")
        elif pressed[pygame.K_LEFT]:
            print("gauche")
        elif pressed[pygame.K_RIGHT]:
            print("droite")

    def recup_input_manette(self):

        dpad_value = self.joystick.get_hat(0)
        bouton_A = self.joystick.get_button(0)
        bouton_B = self.joystick.get_button(1)
        bouton_X = self.joystick.get_button(2)
        bouton_Y = self.joystick.get_button(3)

        if dpad_value == (0, 1):
            print("D-pad vers le haut")
        elif dpad_value == (0, -1):
            print("D-pad vers le bas")
        elif dpad_value == (-1, 0):
            print("D-pad vers la gauche")
        elif dpad_value == (1, 0):
            print("D-pad vers la droite")
        elif bouton_A:
            print("bouton A")
        elif bouton_B:
            print("bouton B")
        elif bouton_X:
            print("bouton X")
        elif bouton_Y:
            print("bouton Y")

    def run(self):
        running = True

        while running:
            self.recup_input_clavier()
            self.recup_input_manette()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()