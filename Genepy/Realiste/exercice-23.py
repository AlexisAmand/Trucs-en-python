# Attaque d'un coffre fort

from itertools import permutations 
 
# toutes les permutations de [1, 5, 8] avec une longeur de 4
perm = permutations([1, 5, 8] * 2, 4) 
 
# affichage des permutations où 1,5 et 8 sont présents 
for i in list(perm): 
    if 1 in i and 5 in i and 8 in i:
        print(f"{i[0]} {i[1]} {i[2]} {i[3]}")
