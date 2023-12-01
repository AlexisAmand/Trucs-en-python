# Tri faire-valoir (en anglais : Stooge Sort)
# (adapté de l'article dispo sur Wikipedia)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]

# cette fonction fait le tri !

def stoogesort(a_list, i, j):
     if a_list[i] > a_list[j]:
        a_list[i], a_list[j] =  a_list[j], a_list[i]
     if (j - i + 1) > 2:
         t = (j - i + 1) // 3
         stoogesort(a_list, i  , j-t)
         stoogesort(a_list, i+t, j  )
         stoogesort(a_list, i  , j-t)
     return a_list

# On affiche la liste d'origine

print("La liste de départ:")
print(a_list)

# On fait le tri faire-valoir

stoogesort(a_list, 0, len(a_list)-1)
            
# On affiche la liste triée

print("La liste triée avec un tri faire-valoir:")
print(a_list)
