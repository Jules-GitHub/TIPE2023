import pygame

class Vehicule:

    def __init__(self, poids, carburant, vitesse):
        self.poids      = poids
        self.carburant  = carburant
        self.vitesse    = vitesse

    def conso(self):
        return 1