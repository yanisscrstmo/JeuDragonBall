import pygame
from fighter import Fighter

class Combat():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/onlymp3.to - Dragon Ball Z Perfect Cell Theme US. Ver. Epic Cover-4UDapUtM0Kw-192k-1704652578.mp3")
        pygame.mixer.music.play()

        self.screen_width = 1600
        self.screen_height = 595

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("1v1 Dragon Ball Fighter GT")

        self.background_image = pygame.image.load("assets/cellgames.jpg").convert_alpha()

        self.sprite_sheet_p_1 = pygame.image.load("assets/gokussjbluespsh.png").convert_alpha()
        self.sprite_1_steps = [10, 8, 1, 7, 7, 3, 7]




        self.red = (255,0,0)
        self.yellow = (255,255,0)
        self.white = (255,255,255)

        self.joueur_1_size = 162
        self.joueur_1_data = [self.joueur_1_size]
        self.joueur_2_size = 250
        self.joueur_2_data = [self.joueur_2_size]

        self.fighter_1 = Fighter(200, 310,)
        self.fighter_2 = Fighter(1325, 310)




    def background(self):
        self.screen.blit(self.background_image, ((self.screen_width - self.background_image.get_width()) // 2, (self.screen_height - self.background_image.get_height()) // 2))




    def draw_health_bar(self,health,x,y):
        ratio = health / 100
        pygame.draw.rect(self.screen,self.white,(x-2,y-2,404,34))
        pygame.draw.rect(self.screen,self.red,(x,y,400,30))
        pygame.draw.rect(self.screen, self.yellow,(x,y,400 * ratio,30))


    def run(self):
        clock = pygame.time.Clock()

        run = True
        while run:

            self.background()
            self.draw_health_bar(self.fighter_1.health,20,20)
            self.draw_health_bar(self.fighter_2.health, 700, 20)
            self.fighter_1.movement(self.screen_width, self.screen_height,self.screen, self.fighter_2)
            # fighter_2.movement()
            self.fighter_1.draw(self.screen)
            self.fighter_2.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            clock.tick(60)

        pygame.quit()