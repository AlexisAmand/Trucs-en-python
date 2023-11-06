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
    try:    
        n = int(input("Indiquer l'entier positif à tester (0 pour quitter): "))
    except ValueError as e:
        print("Vous devez indiquer un entier strictement positif ! - %s" % e)
    else:     
        if n == 0:
            print("Au revoir !")
            break
        parfait(n)
        




