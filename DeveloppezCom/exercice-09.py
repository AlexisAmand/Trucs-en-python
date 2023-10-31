# tuto dvp.com - exercice 9

# fonction qui calcule la somme due

def amende(poule, chien, vache, ami):
    return 200 - poule - 3 * chien - 5 * vache - 10 * ami




# programme principal

poule = int(input("Combien de poule ? "))
chien = int(input("Combien de chien ? "))
vache = int(input("Combien de vache ? "))
ami = int(input("Combien d'ami ? "))

print(f"La somme due est: {amende(poule, chien, vache, ami)} euros")
