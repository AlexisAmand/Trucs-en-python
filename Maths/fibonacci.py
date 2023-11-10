# Fibonacci

# cette fonction calcule le terme de rang n de la suite de Fibonacci

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)



# programme principal

print("Fibonacci\n")
print("Ce programme affiche les N premiers termes de la suite de Fibonacci\n\n")

while True:         
        try:
            n= int(input("Indiquez une valeur pour N (0 pour quitter): "))
        except ValueError as e:
            print("Vous devez choisir un entier positif. - %s" % e)
        else:   
            if n == 0:
                print("Au revoir !")
                break
            print(f"les {n} premiers termes de la suite de Fibonacci sont:")

            for i in range (0, n):
                print(f"{fibo(i)} ", end="")
            print()
