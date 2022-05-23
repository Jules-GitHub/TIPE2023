import pygame

class Fenetre:

    def __init__(self, largeur, hauteur, fond):
        self.hauteur    = hauteur
        self.largeur    = largeur
        self.fond       = fond
        self.fenetre    = pygame.display.set_mode((largeur, hauteur))

    def ferme(self):
        pygame.quit()

    def update(self):
        pygame.display.flip()

    def change_fond(self, fond):
        self.fond = fond
    
    def reset(self):
        self.fenetre.blit(self.fond, (0,0))
        self.update()

    def affiche(self, image, x, y):
        self.fenetre.blit(image, (x, y))
        self.update()