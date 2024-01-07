import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        self.pos_y = 0
        self.jump = False


    def movement(self,screen_width, screen_height):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0


        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            dx = -speed
        if key[pygame.K_RIGHT]:
            dx = speed


        if key[pygame.K_UP] and self.jump == False:
            self.pos_y = -30
            self.jump = True
        # if key[pygame.K_e] and:


        self.pos_y += gravity
        dy += self.pos_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.pos_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        self.rect.x += dx
        self.rect.y += dy

    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)