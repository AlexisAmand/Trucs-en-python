﻿# Afficher une table de multiplication

# Affichage de la table

def table(m):
    for t in range (1, 11):
        print(f"{t} x {m} = {t * m}")
        
print("Tables de multiplication\n")
print("Ce programme affiche la table de N.\n")



# programme principal

while True:
    try:    
        m = int(input("\nQuelle table voulez vous afficher (0 pour quitter)? "))
    except ValueError as e:   
        print("N doit être un entier positif.! - %s" % e)
    else:
        if m == 0:
            print("Au revoir.")
            break
        print(f"\nVoici la table de {m}:\n")
        table(m)
 
            
        




