from plateau import Plateau
from joueur import Joueur
from pion import Pion

class Partie:

    def __init__(self):
        j1Name = raw_input("Nickname of player 1 : ")
        self.j1 = Joueur(str(j1Name))
        j2Name = raw_input("Nickname of player 2 : ")
        self.j2 = Joueur(str(j2Name))
        self.j1.changeMyTurn()
        self.plateau = Plateau()
        self.plateau.affichagePlateau()

    def putPionInPlateau(self):
        self.plateau = ""

    def startGame(self):
        #Init du plateau
        while(self.gaming()):
            print(self.plateau.affichagePlateau())

    def gaming(self):
        self.j1.changeMyTurn()


