from plateau import Plateau
from joueur import Joueur
from pion import Pion

class Partie:

    def __init__(self):
        j1Name = raw_input("Nickname of player 1 : ")
        self.j1 = Joueur(str(j1Name), "o")
        j2Name = raw_input("Nickname of player 2 : ")
        self.j2 = Joueur(str(j2Name), "x")
        self.j1.changeMyTurn()
        self.plateau = Plateau()

    def putPionInPlateau(self):
        self.plateau = ""

    def startGame(self):
        #Init du plateau
        posX = 0
        posY = 0
        decalage = 0
        for pion in self.j1.myPion:
            self.plateau.ajoutPion(pion, posX, posY)
            posY += 2
            if posY>3:
                if (decalage == 0):
                    decalage = 1
                else :
                    decalage = 0
                posX += 1
                posY = 0+decalage
        decalage = 1
        posY=1
        posX=0
        for pion in self.j2.myPion:
            self.plateau.ajoutPion(pion, posX, posY)
            posY += 2
            if posY>3:
                if (decalage == 0):
                    decalage = 1
                else :
                    decalage = 0
                posX += 1
                posY = 0+decalage

        while(self.gaming()):
            print(self.plateau.affichagePlateau())

    def gaming(self):
        self.plateau.affichagePlateau()
        if(self.j1.monTour):
            print("It's "+self.j1.nom+" turn : \n\r")
            self.plateau.askDeplacement(self.j1.nom)
            self.j1.changeMyTurn()
        elif(self.j2.monTour):
            print("It's "+self.j2.nom+" turn : \n\r")
            self.plateau.askDeplacement(self.j1.nom)
            self.j2.changeMyTurn()

        return True


