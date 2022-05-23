import pygame

from fenetre import Fenetre
from vehicule import Vehicule

fen = Fenetre(500, 400, None)

noir = pygame.image.load("noir.png").convert()

fen.change_fond(noir)

continuer = True
while continuer:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            continuer = False

    fen.update()

fen.ferme()