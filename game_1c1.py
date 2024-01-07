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




    def background(self):
        self.screen.blit(self.background_image, ((self.screen_width - self.background_image.get_width()) // 2, (self.screen_height - self.background_image.get_height()) // 2))

    fighter_1 = Fighter(200, 310)
    fighter_2 = Fighter(1325, 310)

    def run(self):
        clock = pygame.time.Clock()

        run = True
        while run:

            self.background()
            self.fighter_1.movement(self.screen_width, self.screen_height)
            # fighter_2.movement()
            self.fighter_1.draw(self.screen)
            self.fighter_2.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            clock.tick(60)

        pygame.quit()