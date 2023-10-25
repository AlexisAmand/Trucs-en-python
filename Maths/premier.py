# Ce nombre est-il premier ?

# J'ai adapté mon script qui recherche les divisieurs

def diviseurs(x):
    divs = list()
    for i in range (1, x+1):
        if x%i == 0:
            divs.append(i)
    return divs

# Uniquement pour voir si le test est fini

fini = False

# On demande à un entier à l'utilisateur
# Il faut vérifier que x est bien une série de chiffres avec isdigit()

# Un nombre N est premier s'il a uniquement 2 diviseurs : 1 et N
        
while fini == False:
    x = input("Indiquez un entier: ")
    if(x.isdigit()):
        if len(diviseurs(int(x))) == 2:
            print(f"{x} est premier !")
            fini = True
        else:
            print(f"{x} n'est pas premier !")
            fini = True
    else:
        print("Merci d'indiquez un nombre entier !")
