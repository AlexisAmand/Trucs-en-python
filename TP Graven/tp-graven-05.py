# Tuto 05 de Graven : le juste prix

import random

# Choisir un nombre entre 1 et 1000
prix = random.randint(1,1000)

# Tant que le jeu n'est pas fini
# -> demander à l'utilisateur "Entrer un prix"

proposition = 0

while proposition != prix:
    proposition = int(input("Entrer un prix :"))
    
    # -> s'il trouve le juste prix "c'est gagné !"
    if proposition == prix:
        print ("C'est gagné !")
        
# -> sinon on affiche "c'est moins" ou "c'est plus"
    elif proposition < prix:
        print("C'est plus")
    elif proposition > prix:
        print("C'est moins")
        


