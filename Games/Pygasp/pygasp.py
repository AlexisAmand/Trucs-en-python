# Le Gasp

import os

# nombre de coups déjà joué

nb_coup, n, x_count = 0, 6, 6
damier = []

# effacer l'écran
def clearscreen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')



# Initialisation du damier

def initialisation_damier():
    global damier
    for ligne in range(n):
        ligne_damier = []  
        for colonne in range(n):
            ligne_damier.append("0")  
        damier.append(ligne_damier) 

   

# Cette fonction affiche le tableau de jeu

def affiche_damier():            
    print("  1 2 3 4")
    for ligne in range(1 ,n-1):
        print(ligne, end=" ")
        for colonne in range(1, n-1):
            print(damier[ligne][colonne], end=" ")
        print()  



# On vérifier si le joueur a gagné

def verification_damier():
        global x_count
        x_count = 0
        for ligne in range(1,n-1):
            for colonne in range(1,n-1):
                if damier[ligne][colonne] == "X":
                    x_count +=1        
        if x_count == 16:
            return True
        else:
            return False



# écran de présentation

clearscreen()
print("-------")
print("Le Gasp")
print("-------\n\n")

print("Le Gasp est un petit jeu de réflexion qui est un petit mélange de Reverso et d'Othello. Vous disposez d'un plateau de jeu avec 16 pions formant un carré 4 x 4. Le but est de tous les retourner en respectant une seule règle : Quand vous désignez un pion, ses 8 voisins sont retournés sauf lui. Saurez-vous toutes les retourner ?")

input("\n\nAppuyez sur entrée pour continuer.")

# nouvelle partie ! Le damier est remis à zéro

clearscreen()
initialisation_damier()
affiche_damier()

# tour de jeu
# par défaut, on considère que le joueur a perdu
# on boucle donc... tant qu'il n'a pas gagné

while x_count != 16:
    
    # coup du joueur
    
    print(f"\nVous avez déjà joué {nb_coup} coup(s).")
    coup = input("Votre coup (colonne, ligne)): ")
    nb_coup += 1
    
    # récupération des coordonnées du pion choisi
    # comme en maths : x pour les colonnes, y pour les lignes

    coup = coup.split(",")     
    x = int(coup[0])
    y = int(coup[1])
    
    # on retourne les pions autour de celui choisi
    for colonne in range(x-1,x+2): 
        for ligne in range(y-1,y+2):   
            if damier[colonne][ligne] == "0":
                damier[colonne][ligne] = "X"
            elif damier[colonne][ligne] == "X":
                damier[colonne][ligne] = "0"
        
    # mais le pion choisi le change pas

    if damier[x][y] == "0":
        damier[x][y] = "X"
    elif damier[x][y] == "X":
        damier[x][y] = "0"

    # vérification si le joueur a gagné

    if verification_damier():
        print(f"\nC'est gagné en {nb_coup} coups !\n")
    else:
        clearscreen()
        affiche_damier()
    