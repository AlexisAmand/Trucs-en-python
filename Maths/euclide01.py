# Trouver le PGCD de deux entiers
# (Méthode 1)

import sys
import math

# L'algo d'Euclide !

def euclide(a, b):
    while b != 0:
        a, b = b, a % b
    return a        

# Progamme principal

print("Trouvons le PGCD de deux entiers !")

a = int(input("Indiquer la valeur du 1er entier : "))
b = int(input("Indiquer la  valeur du 2e entier : "))

print(f"\nLe PGCD de {a} et {b} est  {euclide(a,b)}\n")