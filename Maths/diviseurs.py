# Liste des diviseurs d'un entier

# cette fonction cherche les diviseurs et les met dans une liste

def diviseurs(x):
    divs = list()
    for i in range (1, x+1):
        if x%i == 0:
            divs.append(i)
    return divs


# programme principal
        
while True:
    try:
        x = int(input("Indiquez un entier (0 pour quitter): "))   
    except ValueError as e:
        print("Vous devez choisir un entier positif. - %s" % e)
    else:
        if x == 0:
            print("Au revoir !")
            break
        print(f"La liste des diviseurs de {x} est {diviseurs(x)}")