import pygame

black = (0,0,0)
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