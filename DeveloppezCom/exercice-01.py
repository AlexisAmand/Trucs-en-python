# tuto dvp.com - exercice 1

# pour avoir la valeur de pi dans la suite
import math

# on demande les valeurs à l'utilisateur
rayon = float(input("Quel est le rayon de la base ? "))
hauteur = float(input("Quel est la hauteur ? "))

# on fait le calcul
volume = 1/3 * math.pi * rayon * rayon * hauteur

# on affiche la valeur du volume
print(f"le volume est : {volume}")
        