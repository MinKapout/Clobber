from pion import Pion

class Plateau :

    def __init__(self):
        self.plateau = []
        for plateauXY in range(3):
            self.plateau.append([0] and [0]*4)

    def ajoutPion(self, pion, posX, posY):
        if self.plateau[posX][posY] == 0:
            self.plateau[posX][posY] = pion
            return True
        else:
            return False

    def affichagePlateau(self):
        strLigne = "- - - - - - - - -\n\r"

        strToRet = ""
        strToRet += strLigne

        for posX in range(3):
            for posY in range(4):
                if(self.plateau[posX][posY] == 0):
                    strToRet += "|   "
                else:
                    strToRet += "| "+self.plateau[posX][posY].getImgCase()+" "
            strToRet+="|\n\r"+strLigne

        print(strToRet)

    def askDeplacement(self, nom):
        posXPion = int(raw_input("Pion hote : \n\r Pion posX : "))
        posYPion = int(raw_input("Pion posY : "))

        #Verification de l'entre hote
        while(posXPion > 3 or posYPion > 4 ):
            print("Position en dehors du plan")
            posXPion = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYPion = int(raw_input("Pion posY : "))

        while(self.plateau[posXPion][posYPion] == 0):
            print("C'est une case vide")
            posXPion = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYPion = int(raw_input("Pion posY : "))

        while(not self.plateau[posXPion][posYPion].owner.nom == nom):
            print("Ce pion ne vous appartient pas")
            posXPion = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYPion = int(raw_input("Pion posY : "))

        while((not (self.plateau[posXPion][posYPion+1] == 0)) or (not (self.plateau[posXPion][posYPion-1] == 0)) or (not (self.plateau[posXPion+1][posYPion] == 0)) or (not ((self.plateau[posXPion-1][posYPion] == 0)))):
            print("Cette hote ne peut pas avoir d'enemies")
            posXPion = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYPion = int(raw_input("Pion posY : "))


        print("\n\r")
        #Verification de l'entre cible
        posXCible = int(raw_input("Pion cible : \n\r Pion posX : "))
        posYCible = int(raw_input("Pion posY : "))
        while(posXCible > 3 or posYCible > 4 ):
            print("Position en dehors du plan")
            posXCible = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYCible = int(raw_input("Pion posY : "))

        while(self.plateau[posXCible][posYCible] == 0):
            print("Ce pion ne vous appartient pas")
            posXCible = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYCible = int(raw_input("Pion posY : "))

        while(self.plateau[posXCible][posYCible].owner.nom == nom):
            print("C'est une case vide")
            posXCible = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYCible = int(raw_input("Pion posY : "))

        while(((posXCible==(posXPion+1) or posXCible==(posXPion-1)) and (posYCible == posYPion)) or ((posYCible==(posYPion+1) or posYCible==(posYPion-1)) and (posXCible == posXPion))):
            print("La cible n'est pas a proximite de l'hote")
            posXCible = int(raw_input("Pion selection : \n\r Pion posX : "))
            posYCible = int(raw_input("Pion posY : "))

        self.plateau[posXCible][posYCible] = self.plateau[posXPion][posYPion]
        self.plateau[posXPion][posYPion] = 0

        return True


