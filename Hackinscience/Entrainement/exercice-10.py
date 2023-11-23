# Les nombres pernicieux

# Un nombre est-il premier ?
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
        

# Affiche les pernicieux sur un interval donné

def pernicieux(a, b):
    for i in range(a, b):
        count = 0
        i_binaire = bin(i)
        i_binaire_sans_b = i_binaire[2:]
        for k in i_binaire_sans_b:
            if k == "1":
                count += 1
        if is_prime(count):
            print(i)

# Test pour l'interval allant de 222281 à 222381

pernicieux(222281, 222381)
    