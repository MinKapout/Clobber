from pion import Pion

class Plateau :

    def __init__(self):
        self.plateau = []
        for plateauXY in range(3):
            self.plateau.append([0] and [0]*4)

    def ajoutPion(self, pion, posX, posY):
        if [posX] and posY == 0:
            self.plateau[posX][posY] = pion
            return True
        else:
            return False

    def affichagePlateau(self):
        self.plateau()

