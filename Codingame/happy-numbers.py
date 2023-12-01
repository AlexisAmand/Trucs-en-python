# Puzzle : Happy Numbers

import sys
import math

# note : un théorème dit que quelque soit le nombre entier strictement positif de départ, 
# en calculant successivement la somme des carrés des chiffres, on atteint nécessairement 1 ou 4

n = int(input())
for i in range(n):
    x = int(input())

    nombre = x

    while x != 1 and x != 4:
        happy = 0
        for chiffre in str(x):
            happy = happy + (int(chiffre) * int(chiffre))
        x = happy

    if x == 1:
        print(nombre, ":)")
    else:
        print(nombre, ":(")
