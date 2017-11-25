from pion import Pion

class Joueur:

    def __init__(self, nom, imgCase):
        self.nom = nom
        self.monTour = False
        self.myPion = []
        for idPion in range(6):
            self.myPion.append(Pion(idPion, imgCase, self))

    def changeMyTurn(self):
        if(self.monTour):
            self.monTour = False
        else:
            self.monTour = True
        return self.monTour

