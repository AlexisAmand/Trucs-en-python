# Trouver à quel nombre pense d'ordinateur

import random

# Niveau de difficulté
level = int(input(f"Niveau de difficulté (1/2/3) : "))
min = 1
max = level * 25

# Valeur aléatoire du nombre à trouver
numberToFind  = random.randint(min,max)

numberUser = 0
nbCoup = 0

# Début de la partie
print(f"Je pense à un nombre entre {min} et {max}...")

while numberUser != numberToFind:
    try:
        numberUser = int(input("Proposez une valeur :"))
    except ValueError as e:
        print("Vous devez choisir un entier positif. - %s" % e)
    else:
        nbCoup = nbCoup + 1
        if numberUser < numberToFind:
            print("Le nombre est plus grand !")
        elif numberUser > numberToFind:
            print("Le nombre est plus petit !")

# Le joueur a gagné !
print(f"Bravo ! Le nombre à trouver était {numberToFind}.")
print(f"Vous avez trouvé en {nbCoup} coup(s).")
