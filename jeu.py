import pygame
import sqlite3
import pytmx
import pyscroll

base_donnees = sqlite3.connect("game_datas.db")
curseur = base_donnees.cursor()
joueur_1 = 'GOKU'

curseur.execute("SELECT PV FROM Stats")
pv = curseur.fetchone()[0]

curseur.execute("SELECT ATT_MIN FROM Stats")
att_min = curseur.fetchone()[0]

curseur.execute("SELECT ATT_MAX FROM Stats")
att_max = curseur.fetchone()[0]

pv_goku = curseur.execute("SELECT PV FROM Stats WHERE NOM LIKE ?", (joueur_1,)).fetchone()[0]


print((pv_goku))


pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/Unmei no Hi (Instrumental).mp3")
pygame.mixer.music.play()

son_clic = pygame.mixer.Sound("assets/cliqué.wav")

screen_width = 1800
screen_height = 595

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon Ball FighterGT")

background_image = "assets/cellgames.jpg"
background = pygame.image.load(background_image).convert()

class Player_infos():
    def __init__(self, screen, font):
        self.curseur = curseur
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.rect_p2 = player2_rect
        self.screen = screen
        self.font = font
        self.pv_joueur_1 = 0
        self.pv_joueur_2 = 0
        self.att_min_joueur_1 = 0
        self.att_min_joueur_2 = 0
        self.att_max_joueur_1 = 0
        self.att_max_joueur_2 = 0

    def player_health(self):
        self.pv_joueur_1 = self.curseur.execute("SELECT PV FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
        self.pv_joueur_2 = self.curseur.execute("SELECT PV FROM Stats WHERE NOM  LIKE ?", (self.joueur_2,)).fetchone()[0]

    def player_attack(self):
        self.att_min_joueur_1 = self.curseur.execute("SELECT ATT_MIN FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
        self.att_min_joueur_2 = self.curseur.execute("SELECT ATT_MIN FROM Stats WHERE NOM LIKE ?", (self.joueur_2,)).fetchone()[0]
        self.att_max_joueur_1 = self.curseur.execute("SELECT ATT_MAX FROM Stats WHERE NOM LIKE ?", (self.joueur_1,)).fetchone()[0]
        self.att_max_joueur_2 = self.curseur.execute("SELECT ATT_MAX FROM Stats WHERE NOM LIKE ?", (self.joueur_2,)).fetchone()[0]

    def afficher(self, rect_p2):
        self.player_health()
        texte_surface = self.font.render(f"Pv Joueur 2: {str(self.pv_joueur_2)}", True, (255, 255, 255))
        texte_rect = texte_surface.get_rect(midtop=(self.rect_p2.centerx, self.rect_p2.top - 10))


class Player1(pygame.sprite.Sprite):
    def __init__(self, pv, att_min, att_max, player2_image):
        super().__init__()
        self.pv = pv
        self.att_min = att_min
        self.att_max = att_max
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(player2_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, (screen_height - self.rect.height) // 2)

    def player_return(self):
        return self.image, self.rect

class Player2(pygame.sprite.Sprite):
    def __init__(self, pv, att_min, att_max, player2_image):
        super().__init__()
        self.pv = pv
        self.att_min = att_min
        self.att_max = att_max
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(player2_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (self.screen_width - 5, (self.screen_height - self.rect.height) // 2)

    def player_return(self):
        return self.image, self.rect

class Interface():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def dessiner_bouton(self, rect, color, text, icone=None):
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, black, rect, 2)
        if icone:
            icone_rect = icone.get_rect(topleft=(rect.left + 5, rect.centery - icone.get_height() // 2))
            self.screen.blit(icone, icone_rect)
        texte_surface = self.font.render(text, True, black)
        texte_rect = texte_surface.get_rect(midleft=(rect.left + 55, rect.centery))
        self.screen.blit(texte_surface, texte_rect)


player1 = Player1(pv, att_min, att_max, "assets/vegetassj4_G.png")
player1_image, player1_rect = player1.player_return()
screen.blit(player1_image, player1_rect)

player2 = Player2(pv, att_min, att_max, "assets/vegetassj4.png")
player2_image, player2_rect = player2.player_return()
screen.blit(player2_image, player2_rect)

        #Goku SSJ 4 Gauche
# goku_ssj_4_image = "gokussj4.png"
# goku_ssj_4 = pygame.image.load(goku_ssj_4_image).convert_alpha()
# goku_ssj_4_rectangle = goku_ssj_4.get_rect()
# goku_ssj_4_rectangle.topleft = (5, (screen_height - goku_ssj_4_rectangle.height) // 2)

player1 = Player1(pv, att_min, att_max, "assets/vegetassj4_G.png")
player2 = Player2(pv, att_min, att_max, "assets/vegetassj4.png")

# #Vegeta SSJ 4 Gauche
# vegeta_ssj_4_G_image = "assets/vegetassj4_G.png"
# vegeta_ssj_4_G = pygame.image.load(vegeta_ssj_4_G_image).convert_alpha()
# vegeta_ssj_4_G_rectangle = vegeta_ssj_4_G.get_rect()
# vegeta_ssj_4_G_rectangle.topleft = (5, (screen_height - vegeta_ssj_4_G_rectangle.height) // 2 + 30)

# Vegeta SSJ 4 Droite
# vegeta_ssj_4_image = "vegetassj4.png"
# vegeta_ssj_4 = pygame.image.load(vegeta_ssj_4_image).convert_alpha()
# vegeta_ssj_4_rectangle = vegeta_ssj_4.get_rect()
# vegeta_ssj_4_rectangle.topright = (screen_width - 5, (screen_height - vegeta_ssj_4_rectangle.height) // 2 + 30)

# #Goku SSJ 4 Droite
# goku_ssj_4_D_image = "gokussj4_D.png"
# goku_ssj_4_D = pygame.image.load(goku_ssj_4_D_image).convert_alpha()
# goku_ssj_4_D_rectangle = goku_ssj_4_D.get_rect()
# goku_ssj_4_D_rectangle.topright = (screen_width - 5, (screen_height - goku_ssj_4_rectangle.height) // 2)

#Baby Gauche
baby_G_image = "assets/baby_G.png"
baby_G = pygame.image.load(baby_G_image).convert_alpha()
baby_G_rectangle = baby_G.get_rect()
baby_G_rectangle.topleft = (5, (screen_height - baby_G_rectangle.height) // 2 + 10)

#Baby Droite
baby_D_image = "assets/baby_D.png"
baby_D = pygame.image.load(baby_D_image).convert_alpha()
baby_D_rectangle = baby_D.get_rect()
baby_D_rectangle.topright = (screen_width - 5, (screen_height - baby_D_rectangle.height) // 2 + 10)

#Pan Gauche
pan_G = pygame.image.load("assets/pan_G.png").convert_alpha()
pan_G_rectangle = pan_G.get_rect()
pan_G_rectangle.topleft = (5, (screen_height - baby_G_rectangle.height) // 2)

#Pan Droite
pan_D = pygame.image.load("assets/pan_D.png").convert_alpha()
pan_D_rectangle = pan_D.get_rect()
pan_D_rectangle.topright = (screen_width - 5, (screen_height - baby_D_rectangle.height) // 2)

#Super 17 Gauche
super17_G = pygame.image.load("assets/super17.png").convert_alpha()
super17_G_rectangle = super17_G.get_rect()
super17_G_rectangle.topleft = (5, (screen_height - super17_G_rectangle.height) // 2)

#Super 17 Droite

#Cell GT Gauche
cell_G = pygame.image.load("assets/cell.png").convert_alpha()
cell_G_rectangle = super17_G.get_rect()
cell_G_rectangle.topleft = (5, (screen_height - cell_G_rectangle.height) // 2)

#Hercule Gauche
herc_G = pygame.image.load("assets/hercule.png").convert_alpha()
herc_G_rectangle = herc_G.get_rect()
herc_G_rectangle.topleft = (5, (screen_height - herc_G_rectangle.height) // 2)

#Icône Vegeta SSJ 4
icone_image_vegeta_ssj4 = pygame.image.load("assets/iconevegetassj4.png").convert_alpha()
icone_vegeta_ssj_4_taille = (50, 50)
icone_image_vegeta_ssj4 = pygame.transform.scale(icone_image_vegeta_ssj4, icone_vegeta_ssj_4_taille)

#Icône Goku ssj 4
icone_image = pygame.image.load("assets/iconegokussj4.png").convert_alpha()
icone_taille = (50, 50)
icone_image = pygame.transform.scale(icone_image, icone_taille)

#Icône Baby
icone_image_baby = pygame.image.load("assets/iconebaby.png").convert_alpha()
icone_baby_taille = (50, 50)
icone_image_baby = pygame.transform.scale(icone_image_baby, icone_baby_taille)

#Icône Pan
icone_image_pan = pygame.image.load("assets/iconepan.png").convert_alpha()
icone_pan_taille = (50, 50)
icone_image_pan = pygame.transform.scale(icone_image_pan, icone_pan_taille)

#Icône Hercule
icone_image_herc = pygame.image.load("assets/iconehercule.png").convert_alpha()
icone_herc_taille = (50, 50)
icone_image_herc = pygame.transform.scale(icone_image_herc, icone_herc_taille)

#Bannière Goku SSJ 4
ban_goku = pygame.image.load("assets/gokuban.png").convert_alpha()
ban_goku_rectangle = ban_goku.get_rect()
ban_goku_rectangle.center = (1800 // 2, 595 // 2)

#Bannière Vegeta SSJ 4
ban_vegeta = pygame.image.load("assets/vegetaban.png").convert_alpha()
ban_vegeta_rectangle = ban_vegeta.get_rect()
ban_vegeta_rectangle.center = (1800 // 2, 595 // 2)

#Bannière Baby
ban_baby = pygame.image.load("assets/babyban.png").convert_alpha()
ban_baby_rectangle = ban_baby.get_rect()
ban_baby_rectangle.center = (1800 // 2, 595 // 2)

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)



font = pygame.font.Font(None, 36)
# def dessiner_bouton(rect, color, text, icone=None):
#     pygame.draw.rect(screen, color, rect)
#     pygame.draw.rect(screen, black, rect, 2)
#     if icone:
#         icon_rect = icone.get_rect(topleft=(rect.left + 5, rect.centery - icone.get_height() // 2))
#         screen.blit(icone, icon_rect)
#     texte_surface = font.render(text, True, black)
#     texte_rect = texte_surface.get_rect(midleft=(rect.left + 55, rect.centery))
#     screen.blit(texte_surface, texte_rect)

bouton_hercule_rect = pygame.Rect(600, 140, 220, 50)
bouton_goku_ssj4_rect = pygame.Rect(600, 200, 220, 50)
bouton_vegeta_ssj_4_rect = pygame.Rect(1000, 200, 220, 50)
bouton_baby_rect = pygame.Rect(600, 260, 220, 50)
bouton_pan_rect = pygame.Rect(1000, 260, 220, 50)
bouton_super_17_rect = pygame.Rect(600, 320, 220, 50)
bouton_cell_rect = pygame.Rect(1000, 320, 220, 50)

montrerg_G = False
montrerv_G = False
montrerb_G = False
montrerp_G = False
montrerg_D = False
montrerv_D = False
montrerb_D = False
montrerp_D = False
montrers_G = False
montrers_D = False
montrerc_G = False
montrerh_G = False
joueur1_selectionne = False
joueur2_selectionne = False
joueur_1 = ""
joueur_2 = ""
interface = Interface(screen, font)
infos_player = Player_infos(screen, font)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_goku_ssj4_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerg_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_vegeta_ssj_4_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerv_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_baby_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerb_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_pan_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerp_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_super_17_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrers_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_cell_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerc_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_hercule_rect.collidepoint(event.pos) and not joueur1_selectionne:
                montrerh_G = True
                joueur1_selectionne = True
                son_clic.play()
            elif bouton_goku_ssj4_rect.collidepoint(event.pos) and joueur1_selectionne and not joueur2_selectionne:
                montrerg_D = True
                joueur2_selectionne = True
                son_clic.play()
            elif bouton_vegeta_ssj_4_rect.collidepoint(event.pos) and joueur1_selectionne and not joueur2_selectionne:
                montrerv_D = True
                joueur2_selectionne = True
                son_clic.play()
            elif bouton_baby_rect.collidepoint(event.pos) and joueur1_selectionne and not joueur2_selectionne:
                montrerb_D = True
                joueur2_selectionne = True
                son_clic.play()
            elif bouton_pan_rect.collidepoint(event.pos) and joueur1_selectionne and not joueur2_selectionne:
                montrerp_D = True
                joueur2_selectionne = True
                son_clic.play()

    screen.blit(background, (0, 0))
    interface.dessiner_bouton(bouton_goku_ssj4_rect, gray, "Goku SSJ 4", icone_image)
    interface.dessiner_bouton(bouton_vegeta_ssj_4_rect, gray, "Vegeta SSJ 4", icone_image_vegeta_ssj4)
    interface.dessiner_bouton(bouton_baby_rect, gray, "Super Baby 1", icone_image_baby)
    interface.dessiner_bouton(bouton_pan_rect, gray, "Pan", icone_image_pan)
    interface.dessiner_bouton(bouton_super_17_rect, gray, "Super C-17", icone_image_baby)
    interface.dessiner_bouton(bouton_cell_rect, gray, "Cell GT", icone_image_pan)
    interface.dessiner_bouton(bouton_hercule_rect, gray, "Hercule", icone_image_herc)



    #afficher_vies(black, pv)

    if montrerg_G:
        player2_image, player2_rect = player2.player_return()
        screen.blit(player2_image, player2_rect)
        joueur_1 = "goku_ssj_4"
    if montrerv_G:
        joueur_1 = 'VEGETA'
        player1_image, player1_rect = player1.player_return()
        screen.blit(player1_image, player1_rect)

    elif montrerb_G:
        screen.blit(baby_G, baby_G_rectangle)
        joueur_1 = "baby_G"
    elif montrerp_G:
        screen.blit(pan_G, pan_G_rectangle)
        joueur_1 = "pan_G"
    elif montrers_G:
        screen.blit(super17_G, super17_G_rectangle)
        joueur_1 = "super_17"
    elif montrerc_G:
        screen.blit(cell_G, cell_G_rectangle)
        joueur_1 = "cell"
    elif montrerh_G:
        screen.blit(herc_G, herc_G_rectangle)
        joueur_1 = "hercule"

    # if montrerg_D:
    #     screen.blit(goku_ssj_4_D, goku_ssj_4_D_rectangle)
    #     joueur_2 = "goku_ssj_4_D"
    if montrerv_D:
        joueur_2 = 'VEGETA'
        player2_image, player2_rect = player2.player_return()
        screen.blit(player2_image, player2_rect)
        infos_player.afficher(player2_rect)
    if montrerb_D:
        screen.blit(baby_D, baby_D_rectangle)
        joueur_2 = "baby_D"
    elif montrerp_D:
        screen.blit(pan_D, pan_D_rectangle)
        joueur_2 = "pan_D"


    """if joueur_1 == "goku_ssj_4":
        screen.blit(ban_goku, ban_goku_rectangle)
    elif joueur_1 == "vegeta_ssj_4":
        screen.blit(ban_vegeta, ban_vegeta_rectangle)
    elif joueur_1 == "baby_G":
        screen.blit(ban_baby, ban_baby_rectangle)"""

    pygame.display.flip()
    pygame.time.Clock().tick(30)

base_donnees.close()
pygame.quit()
quit()