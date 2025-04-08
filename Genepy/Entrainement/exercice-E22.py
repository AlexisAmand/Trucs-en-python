# Triangle de Pascal

# fonction pour calculer une factorielle

def factorielle(x):
    if x == 0:
        return 1
    else:
        facto = 1
        for i in range(2, x+1):
            facto = facto * i
    return facto

# fonction qui affiche le triangle de pascal

def print_pascal_triangle(n):
    size = 2 * n + 1 
    for n in range(n):
        affichage = ""
        for k in range(n+1):
            resultat = int(factorielle(n)/(factorielle(k) * factorielle(n-k)))                
            affichage = affichage + " " + str(resultat)                          
        print(affichage.center(size, ' '))                    
    


# test pour 5 lignes
print_pascal_triangle(5)
