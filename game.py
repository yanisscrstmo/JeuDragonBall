import pygame
import pytmx
import pyscroll
import sqlite3
from pygame.locals import *
from player import Player
from game_1c1 import Combat

base_donnees = sqlite3.connect("game_datas.db")
curseur = base_donnees.cursor()

pygame.mixer.init()
kamehameha = pygame.mixer.Sound("assets/kamehameha-sound-effects-made-with-Voicemod-technology.mp3")

class Jeu:
    def __init__(self):
        self.screen = pygame.display.set_mode((840, 480))
        pygame.display.set_caption("Dragon Ball FighterGT")

        tmx_data = pytmx.util_pygame.load_pygame("map_assets/real_map.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_calques = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_calques.zoom = 2

        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y,"assets/sprites/Goku_MUI.png")
        self.player.resize(29,45,[34,177,76])

        self.murs = []
        self.spawn_points = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                rect_collision = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.murs.append(rect_collision)
            if obj.type == "spawn_point":
                rect_spawn = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.spawn_points.append(rect_spawn)

        print(self.murs)
        print(self.spawn_points)

        self.group = pyscroll.PyscrollGroup(map_layer=map_calques, default_layer=5)
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

    # def gestion_collisions(self):
    #     for mur in self.murs:

    def update(self):
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.spawn_points) > -1:
                jeu1c1 = Combat()
                jeu1c1.run()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.murs) > -1:
                sprite.move_back()




    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:
            self.player.save_location()
            self.recup_input_clavier()
            self.recup_input_manette()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()

base_donnees.close()