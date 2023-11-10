# Trouver le PGCD de deux entiers
# (Méthode 2)

import sys
import math

# L'algo d'Euclide !
# Il y a plus simple, on pourait juste faire return euclide(b, a % b) sans le while !

def euclide(a, b):
    if b == 0:
        return a
    return euclide(b , a % b)

        

# Progamme principale

print("Trouvons le PGCD de deux entiers !")

a = int(input("Indiquer la valeur du 1er entier : "))
b = int(input("Indiquer la  valeur du 2e entier : "))

print(f"\nLe PGCD de {a} et {b} est  {euclide(a,b)}\n")