# tuto dvp.com - exercice 5

x , n, fois = 0, 0, 0

# on demande un nombre à l'utilisateur

while n < 1:
    n = int(input("Entrez un nombre: "))    
    if n < 1:
        print("Il faut qu'il soit strictement positif !")
       
# on teste la division par 2

x = n

while n%2 == 0:
    fois += 1
    n = n / 2
    
# on affiche la réponse
    
print(f"{x} est {fois} fois divisible par 2.")