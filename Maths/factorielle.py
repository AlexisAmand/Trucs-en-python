# Calcul de la factorielle d'un entier

# fonction qui fait le calcul

def factorielle(x):
    if x == 0:
        return 1
    else:
        facto = 1
        for i in range(2, x+1):
            facto = facto * i
    return facto

# on demande un entier à l'utilisateur
# normalement il faut faire une vérification
# x est-il bien en entier ?

x = int(input("Indiquez un entier: "))   
print(f"La factorielle de {x} est {factorielle(x)}.")