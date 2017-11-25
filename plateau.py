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

