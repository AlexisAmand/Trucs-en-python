# tuto dvp.com - exercice 3

# Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. 
# Comptez combien il y avait de données et combien étaient supérieures à 100.

# Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.

total = 0
big_numbers_count = 0
x = 1

while x > 0:
    
    # on demande une valeur
    x = int(input("Entrez une valeur: "))    
    
    # on fait le total
    total = total + x
    
    # test si x > 100
    if x > 100:
        big_numbers_count += 1
        
print(f"La somme des nombres est {total}.")
print(f"Il y avait {big_numbers_count} nombre(s) supérieur(s) à 100.")