# Un nombre est-il premier ?

# La fonction qui fait le boulot
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



# On demande un entier à l'utilisateur
# Il faut vérifier que x est bien une série de chiffres avec isdigit()
        
while True:
    try:
        x = int(input("Indiquez un entier (0 pour quitter): "))
    except ValueError as e: 
        print("Merci d'indiquez un nombre entier !")
    else:
        if x == 0:
            print('fin du programme.\n')
            break
        
        if is_prime(x):
            print(f"{x} est premier !")
        else:
            print(f"{x} n'est pas premier !")  