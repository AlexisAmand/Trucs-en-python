# Trouver le PPCM de deux entiers

import sys
import math

# Une formule dit : ppcm(a, b) = |ab| / PGCD(a,b)
# Cette fonction calcul donc le PGCD

def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b , a % b)

        

# Progamme principale

print("Trouvons le PPCM de deux entiers !")

a = int(input("Indiquer la valeur du 1er entier : "))
b = int(input("Indiquer la  valeur du 2e entier : "))

pgcd = pgcd(a,b)
ppcm = int(abs(a * b) / pgcd)

print(f"\nLe PPCM de {a} et {b} est  {ppcm}\n")