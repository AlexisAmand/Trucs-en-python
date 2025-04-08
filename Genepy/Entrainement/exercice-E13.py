# Est-il divisible par… ?

for i in range(0, 1001):
    # divisible par 7 ?
    somme = 0
    if i % 7 == 0:
        # Oui ! On fait la somme des chiffres.
        for x in str(i):
            somme += int(x) 
        # On vérifie si le résultat est divisible par 3
        if somme % 3 == 0:
            print(i)