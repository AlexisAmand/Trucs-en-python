# Tri par insertion
# (adapté d'un programme en Pascal)

# Une liste pour exemple
# j'ai choisi des mots, mais ça fonctionne avec des entiers

a_list = ["chat", "hibou", "hamster", "chien", "rat", "cheval", "pie", "moineau"]

# On affiche la liste telle est à origine

print("La liste de départ:")
print(a_list)

# On fait le tri par insertion

for i in range(2,len(a_list)):
    j = i - 1
    while j > 0 and a_list[j] > a_list[j + 1]:
        a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        j = j - 1
        
# On affiche le tableau final

print("La liste triée avec un tri par insertion:")
print(a_list)