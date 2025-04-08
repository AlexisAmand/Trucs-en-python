# Afficher tous les premiers d'une intervalle

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a_list = list()

for i in range(10000,10050):   
    if is_prime(i):
        a_list.append(str(i))
          
print(", ".join(a_list))