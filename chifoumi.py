# Jouer à Chifoumi contre l'ordinateur

import random

coups = ["pierre", "papier", "ciseaux"]
joueur_input = False

print("-----------")
print("Chifoumi v1")
print("-----------\n")

manches = int(input("Combien de manches dans la partie ? "))

partie = 1
points_joueur = 0
points_ordi = 0

while partie <= manches:
    
    joueur_input = False
        
    print("\n-----------")
    print(f"Manche n°{partie}")    
    print("-----------\n")
    
    # coup de l'ordinateur
    coup_ordi = random.choice(coups)    

    # coup du joueur
    while joueur_input == False:
        coup_joueur = input("Que jouez vous (pierre/papier/ciseaux) ? ")
        if coup_joueur in coups:
            joueur_input = True
        else:
            print("choix non valide !")
        
    # la partie
    if coup_ordi == coup_joueur:
        print("\négalité !")
        points_ordi += 1
        points_joueur += 1
    elif (coup_ordi == "pierre" and coup_joueur == "ciseaux") or (coup_ordi == "ciseaux" and coup_joueur == "feuille") or (coup_ordi == "feuille" and coup_joueur == "pierre"):
        print(f"\nl'ordinateur a choisi {coup_ordi}, il a gagné !")
        points_ordi += 1
    else:
        print(f"\nl'ordinateur a choisi {coup_ordi}, il a perdu !")
        points_joueur += 1
    
    #affichage des points
    print()
    print(f"score du joueur: {points_joueur}")
    print(f"score de l'ordinateur: {points_ordi}")
    print()  
    
    partie += 1     
    
if points_ordi < points_joueur:
    print("\nC'est le joueur qui gagne cette partie !\n")
else:
    print("\nC'est l'ordinateur qui gagne cette partie !\n")        