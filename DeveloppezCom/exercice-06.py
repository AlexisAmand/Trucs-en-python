# tuto dvp.com - exercice 6

n = 0
liste_diviseurs = list()
result=""

# on demande un nombre à l'utilisateur

while n < 1:
    n = int(input("Entrez un nombre: "))    
    if n < 1:
        print("Il faut qu'il soit strictement positif !")

# On regarde si n est divisible chaque entiers compris en 1 et n
# Si oui, on ajouter le diviseur dans la liste

for i in range (1, n+1):
    if n%i == 0:
        liste_diviseurs.append(i)
            
# si n a 2 diviseurs (1 et N), il est premier 

if len(liste_diviseurs) == 2:
    print(f"Diviseurs propres sans répétition de {n} : aucun ! Il est premier")
else:
    for i in liste_diviseurs:
        result = result + str(i) + " "
    print(f"Diviseurs propres sans répétition de {n} : {result} (soit {len(liste_diviseurs)} diviseurs propres)")         



