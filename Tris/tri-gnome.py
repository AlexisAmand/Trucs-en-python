# Tri gnome
# (adapté de l'article dispo sur Wikipedia)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# On affiche la liste d'origine

print("La liste de départ:")
print(a_list)

# On fait le tri gnome

pos = 0
while pos < len(a_list):
    if (pos == 0 or a_list[pos] >= a_list[pos-1]):   
        pos = pos + 1
    else:
        a_list[pos], a_list[pos-1] = a_list[pos-1], a_list[pos]
        pos = pos - 1

# On affiche la liste triée

print("La liste triée avec un tri gnome:")
print(a_list)