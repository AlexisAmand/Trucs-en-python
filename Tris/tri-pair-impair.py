# Tri pair-impair
# (adapté de l'article dispo sur Wikipedia)

# Une liste pour exemple
# j'ai choisi des mots, mais ça fonctionne avec des entiers

a_list = ["chat", "hibou", "hamster", "chien", "rat", "cheval", "pie", "moineau"]

# On affiche la liste telle est à origine

print("La liste de départ:")
print(a_list)

# On fait le tri pair-impair

for i in range(1,len(a_list) - 1):
    for x in range(1,len(a_list) - 1, 2):
        if a_list[x] > a_list[x+1]:
            a_list[x], a_list[x+1] = a_list[x+1], a_list[x]
    for x in range(0,len(a_list) - 1, 2):
        if a_list[x] > a_list[x+1]:
            a_list[x], a_list[x+1] = a_list[x+1], a_list[x]
            
# On affiche le tableau final

print("La liste triée avec un tri pair-impair:")
print(a_list)
