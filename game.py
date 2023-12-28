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
        self.player = Player(player_position.x,player_position.y,"assets/sprites/Goku_MUI.png")
        self.player.resize(44,67,[34,177,76])

        self.murs = []

        for objet in tmx_data.objects:
            print(objet.type, objet.name, objet.x, objet.y, objet.width, objet.height)
            if objet.type == "collision":
                rect_collision = pygame.Rect(objet.x, objet.y, objet.width, objet.height)
                self.murs.append(rect_collision)

        print(self.murs)

        self.group = pyscroll.PyscrollGroup(map_layer=map_calques, default_layer=3)
        self.group.add(self.player)

        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def recup_input_clavier(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_down()
        elif pressed[pygame.K_DOWN]:
            self.player.move_up()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()

    def recup_input_manette(self):

        dpad_value = self.joystick.get_hat(0)
        bouton_A = self.joystick.get_button(0)
        bouton_B = self.joystick.get_button(1)
        bouton_X = self.joystick.get_button(2)
        bouton_Y = self.joystick.get_button(3)

        if dpad_value == (0, 1):
            self.player.move_down()
        elif dpad_value == (0, -1):
            self.player.move_up()
        elif dpad_value == (-1, 0):
            self.player.move_left()
        elif dpad_value == (1, 0):
            self.player.move_right()
        elif bouton_A:
            print("bouton A")
        elif bouton_B:
            print("bouton B")
        elif bouton_X:
            print("bouton X")
        elif bouton_Y:
            print("bouton Y")

    def gestion_collisions(self):
        for mur in self.murs:


    def run(self):

        clock = pygame.time.Clock()

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

            clock.tick(60)

        pygame.quit()

base_donnees.close()