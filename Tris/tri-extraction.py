# Tri par extraction
# (adapté d'un programme en Pascal)

# Une liste pour exemple
# j'ai choisi des mots, mais ça fonctionne avec des entiers

a_list = ["chat", "hibou", "hamster", "chien", "rat", "cheval", "pie", "moineau"]

# On affiche la liste telle est à origine

print("La liste de départ:")
print(a_list)

# On fait le tri par extraction

for i in range(1, len(a_list) - 1):
    jmin = i
    for j in range(i+1, len(a_list)):
        if a_list[j] < a_list[jmin]:
            jmin = j
    if jmin != i:
        a_list[i], a_list[jmin] = a_list[jmin], a_list[i]

# On affiche le tableau final

print("La liste triée avec un tri par extraction:")
print(a_list)