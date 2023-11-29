# Tri à bulles
# (adapté d'un programme en Pascal)

# Une liste pour exemple
# j'ai choisi des mots, mais ça fonctionne avec des entiers

a_list = ["chat", "hibou", "hamster", "chien", "rat", "cheval", "pie", "moineau"]

# On affiche la liste telle est à origine

print("La liste de départ:")
print(a_list)

# On fait le tri a bulles

for i in range(len(a_list),1,-1):
    for j in range(0,i-1):
        if a_list[j] > a_list[j+1]:            
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

# On affiche le tableau final

print("La liste triée avec un tri à bulles:")
print(a_list)