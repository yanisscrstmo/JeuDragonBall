import pygame

class Fighter():
    def __init__(self,x,y):
        self.flip = False
        self.rect = pygame.Rect((x,y,80,180))
        self.pos_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100


    def movement(self,screen_width, screen_height, surface,target):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0


        key = pygame.key.get_pressed()

        if self.attacking == False:
            if key[pygame.K_LEFT]:
                dx = -speed
            if key[pygame.K_RIGHT]:
                dx = speed


            if key[pygame.K_UP] and self.jump == False:
                self.pos_y = -30
                self.jump = True

            if key[pygame.K_e] or key[pygame.K_r]:
                self.attack(surface,target)
                if key[pygame.K_e]:
                    self.attack_type = 1
                if key[pygame.K_r]:
                    self.attack_type = 2




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

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        self.rect.x += dx
        self.rect.y += dy

    def attack(self,surface,target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2*self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface, (0,255,0),attacking_rect)
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)