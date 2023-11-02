# N est-il un nombre sublime ?

# fonction qui retourne la somme des diviseurs de N

def somme_diviseur(n):
    somme = 0
    for i in range (1, n+1):
        if n%i == 0:
            somme += i
    return somme 

# fonction qui détermine si N est parfait

def parfait(n):
    if somme_diviseur(n) == 2 * n:
        return print(f"{n} est un nombre sublime !")
    else:
        return print(f"{n} n'est pas un nombre sublime !")

# programme principal

print("N est-il un nombre sublime ?\n")

while True:
        n = input("Indiquer l'entier positif à tester (0 pour quitter): ")
        try:
            n = int(n)
            if n == 0:
                break
            parfait(n)            
        except ValueError:
            print("N doit être un entier strictement positif.")
        




