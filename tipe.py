import pygame
from pygame.locals import *

TAILLE = (1060, 863)
DIMENSIONS = (1060, 863)

pygame.init()
fenetre = pygame.display.set_mode(TAILLE)
pygame.display.set_caption("TIPE")


def extraction(fichier):
    plan = []
    _, y = DIMENSIONS
    for i in range(y):
        plan.append(list(fichier.readline().rstrip()))
    print(len(plan), len(plan[0]))
    return plan

def affichage(plan):
    x, y = DIMENSIONS
    blocx = TAILLE[0] // x
    blocy = TAILLE[1] // y
    for i in range(y):
        for j in range(x):
            if plan[i][j] == "1":
                pygame.draw.rect(fenetre, (255,255,255), (j*blocx, i*blocy, blocx, blocy))
            elif plan[i][j] == "0":
                pygame.draw.rect(fenetre, (0,0,0), (j*blocx, i*blocy, blocx, blocy))
    pygame.display.flip()

fichier = open("plan2.txt", "r")
plan = extraction(fichier)
affichage(plan)
print("fini")

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.flip()

pygame.quit()