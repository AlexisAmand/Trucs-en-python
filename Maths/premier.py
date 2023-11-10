# Un nombre est-il premier ?

# J'ai adapté mon script qui recherche les divisieurs

def diviseurs(x):
    divs = list()
    for i in range (1, x+1):
        if x%i == 0:
            divs.append(i)
    return divs



# On demande un entier à l'utilisateur
# Il faut vérifier que x est bien une série de chiffres avec isdigit()

# Un nombre N est premier s'il a uniquement 2 diviseurs : 1 et N
        
while True:
    try:
        x = int(input("Indiquez un entier (0 pour quitter): "))
    except ValueError as e: 
        print("Merci d'indiquez un nombre entier !")
    else:
        if x == 0:
            print('fin du programme.\n')
            break
        
        if len(diviseurs(int(x))) == 2:
            print(f"{x} est premier !")
        else:
            print(f"{x} n'est pas premier !")  