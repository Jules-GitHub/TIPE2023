from voiture import Voiture

class Camion(Voiture):
    def __init__(self, poids, consommation, vitesse, chargement):
        super.__init__(self, poids, consommation, vitesse)
        self.chargement = chargement