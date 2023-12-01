# Tri pair-impair
# (adapté de l'article dispo sur Wikipedia)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# On affiche la liste d'origine

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
            
# On affiche la liste triée

print("La liste triée avec un tri pair-impair:")
print(a_list)
