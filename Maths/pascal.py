﻿# affiche N lignes du Triangle de Pascal
# avec les vérifications pour être sûr que N est un entier

# fonction pour calculer une factorielle

def factorielle(x):
    if x == 0:
        return 1
    else:
        facto = 1
        for i in range(2, x+1):
            facto = facto * i
    return facto



# programme principal

while True:   
    try:
        n = int(input("Combien de lignes voulez-vous afficher (0 pour quitter)? "))
    except ValueError as e:
        print("Vous devez indiquer un entier !- %s" % e)
    else:    
        print()   
        if n == 0:
            print('fin du programme.\n')
            break
        for n in range(n+1):
            for k in range(n+1):
                resultat = int(factorielle(n)/(factorielle(k) * factorielle(n-k)))
                print(f"{resultat} ", end="")
            print()
        print() 
    
   


