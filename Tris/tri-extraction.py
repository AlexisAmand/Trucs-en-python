# Tri par extraction
# (adapté d'un programme en Pascal)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# On affiche la liste d'origine

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

# On affiche la liste triée

print("La liste triée avec un tri par extraction:")
print(a_list)