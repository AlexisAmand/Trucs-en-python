# Trouver à quel nombre pense d'ordinateur

import random

# Valeur minimale du nombre à trouver
min = 1

# Niveau de difficulté
level = int(input(f"Niveau de difficulté (1/2/3) : "))
max = level * 25

# Valeur aléatoire du nombre à trouver
numberToFind  = random.randint(min,max)

numberUser = 0
nbCoup = 0

# Début de la partie
print("Je pense à un nombre...")

while numberUser != numberToFind:
    numberUser = int(input(f"Proposer une valeur entre {min} et {max} :"))
    nbCoup = nbCoup + 1
    if numberUser < numberToFind:
        print("Le nombre est plus grand !")
    elif numberUser > numberToFind:
        print("Le nombre est plus petit !")

# Le joueur a gagné !
print(f"Bravo ! Le nombre à trouver était {numberToFind}.")
print(f"Vous avez trouvé en {nbCoup} coup(s).")
