# tuto dvp.com - exercice 7

# fonction qui calcule la factorielle

def factorielle(x):
    if x == 0:
        return 1
    else:
        facto = 1
        for i in range(2, x+1):
            facto = facto * i
    return facto

# Programme principal

n = int(input("indiquez un entier pour n :"))
e = 0.0
for i in range(n) :
    e = e + 1.0/factorielle(i)

print(f"L'approximation de 'e' est {e:.3f}")




