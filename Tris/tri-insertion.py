﻿# Tri par insertion
# (adapté d'un programme en Pascal)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# On affiche la liste d'origine

print("La liste de départ:")
print(a_list)

# On fait le tri par insertion

for i in range(2,len(a_list)):
    j = i - 1
    while j > 0 and a_list[j] > a_list[j + 1]:
        a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        j = j - 1
        
# On affiche la liste triée

print("La liste triée avec un tri par insertion:")
print(a_list)