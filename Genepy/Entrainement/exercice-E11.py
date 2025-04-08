# Produit d'un itérable

def mul(numbers):
    resultat = 1
    for i in numbers:
        resultat = resultat * i
    return resultat
        
# Tests

print(mul([1, 2, 3]))  # Affiche 6
print(mul([0, 1, 2, 3]))  # Affiche 0 (multiplication par zéro)
print(mul([2, 3, 4]))  # Affiche le résultat de 2 * 3 * 4, soit 24.
print(mul([2, 3, 4]) + mul([1, 2]))  # Affiche le résultat de 2 * 3 * 4 + 1 * 2,  soit 26.
    