# Monnaie

def how_to_pay(amount,currency):

    resultat = {}    

    for i in reversed(sorted(currency)):
        nb = amount // i
        resultat.update({i: nb})
        # la monnaie qu'il reste
        amount -= nb * i

    return resultat



# pour les tests

print(how_to_pay(125, [50, 2, 100,  20, 10, 5]))