# Aimer les ensembles

def love_meet(bob, alice):
    r1 = set()
    for i in bob:
        for j in alice:
            if i == j and i not in r1:
                r1.add(i)
    return r1


def affair_meet(bob, alice, silvester):
    r2 = love_meet(silvester, alice)
    r3 = set()
    for i in r2:
        for j in bob:
            if i in r2 and i not in bob:
                r3.add(i)
    return r3



# pour les tests

alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['ⅩVⅢ', 'XIX', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

print(love_meet(bob, alice))
print(affair_meet(bob, alice, silvester))