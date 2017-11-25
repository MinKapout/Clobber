def newBoard(n,p): #initialisation du plateau
    ligne = n
    colonne = p
    plateau = {[0,1,0,1]
               [0,1,0,1]
               [0,1,0,1]}
    return plateau   #display plateau

def display(plateau,n,p):   #renvoie le plateau sur la console
    for y in range(n):
        for x in range (p):
            print plateau[x,y]
            print('\n')

def possiblePawn(plateau,n,p,i,j): #savoir si le joueur peut se déplacer
    possiblePawn = False
    if possiblePawn == 1:
        return True
    else:
        return False

def possibleDestination(plateau,n,p,player,i,j,k,l): #savoir où il se déplace
    xinter = [i-=1,i,i+=1]
    yinter = [j-=1,i,i+=1]
    if x in xinter and y in yinter:
        return True

