# Calcul de factorielle

def factorielle(x):
    if x == 0:
        return 1
    else:
        facto = 1
        for i in range(2, x+1):
            facto = facto * i
    return facto


x = int(input("Indiquez un entier: "))   
print(f"La factorielle de {x} est {factorielle(x)}.")