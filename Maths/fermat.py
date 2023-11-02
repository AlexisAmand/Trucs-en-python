# Les nombres de Fermat

# cette fonction calcule le nombre de Fermat de rang N

def fermat(n):
    return 2 ** 2 ** n +1

# programme principal

print("Les nombres de Fermat\n")
print("Ce programme affiche les N premiers nombres de Fermat.")
print("Attention ! Un N trop grand nécessite une grosse puissance de calcul !\n\n")

while True:
    n= input("Indiquez une valeur pour N: ") 
    try:
        n = int(n)
        print(f"les {n} premiers nombres de Fermat sont:")
        for i in range (0, n):
            print(f"{fermat(i)} ", end="")
        print()     
        break
    except ValueError:
        print("N doit être un entier positif.")





