# Liste des diviseurs d'un entier

def diviseurs(x):
    divs = list()
    for i in range (1, x+1):
        if x%i == 0:
            divs.append(i)
    return divs
        

x = int(input("Indiquez un entier: "))   
print(f"La liste des diviseurs de {x} est {diviseurs(x)}")