import random

# valeur minimale et maximale du nombre à trouver
min, max  = 1, 50

# valeur aléatoire du nombre à trouver
numberToFind  = random.randint(min,max)

numberUser = 0
nbCoup = 0
while numberUser != numberToFind:
    question = "Proposer une valeur entre 1 et 50 :"
    numberUser = int(input(question))
    nbCoup = nbCoup + 1
    if numberUser < numberToFind:
        print("trop petit !")
    elif numberUser > numberToFind:
        print("trop grand !")
   
print("Vous avez trouvé en", nbCoup , "coup(s).")





