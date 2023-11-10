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


# Programme principal
# On demande un entier à l'utilisateur
# Il faut vérifier que x est bien un entier

while True:
    try:
        x = int(input("Indiquez un entier (0 pour quitter): "))   
    except ValueError as e:
        print("Vous devez choisir un entier positif. - %s" % e)
    else:
        if x == 0:
            print("Au revoir !")
            break 
    print(f"La factorielle de {x} est {factorielle(x)}.")