from pion import Pion

class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.monTour = False
        self.myPion = []
        for idPion in range(6):
            self.myPion.append(Pion(idPion, "x"))

    def changeMyTurn(self):
        if(self.monTour):
            self.monTour = False
        else:
            self.monTour = True
        return self.monTour