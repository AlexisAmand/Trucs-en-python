# Tri à bulles
# (adapté d'un programme en Pascal)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# On affiche la liste d'origine

print("La liste de départ:")
print(a_list)

# On fait le tri a bulles

for i in range(len(a_list),1,-1):
    for j in range(0,i-1):
        if a_list[j] > a_list[j+1]:            
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

# On affiche la liste triée

print("La liste triée avec un tri à bulles:")
print(a_list)