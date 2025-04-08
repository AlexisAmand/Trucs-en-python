# Nombre premier suivant 100 000 000

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

value = 100000000

while not is_prime(value):
    value += 1
    
print(value)