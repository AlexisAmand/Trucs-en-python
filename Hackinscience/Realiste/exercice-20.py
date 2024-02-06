# Présenter des nombres

# pas ouf... mais ça fonctionne

import math

def list_pretty_print(a_list):

    lignes = math.floor(len(a_list) / 5)

    for i in range(lignes):
        listToShow = []
        for k in range(i*5,i*5 + 5):
            listToShow.append(str(a_list[k]))
        print(", ".join(listToShow))

    listToShow = []

    for j in range(lignes * 5, len(a_list)):     
        listToShow.append(str(a_list[j]))
    print(", ".join(listToShow))

# pour les tests 
    
# list_pretty_print([42] * 9)
list_pretty_print([30536, 33705, 43382, 42134, 50380])