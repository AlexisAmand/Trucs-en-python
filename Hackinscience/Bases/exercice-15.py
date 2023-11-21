# Les multiples de 3 et 5

n = 0
somme = 0

for n in range(0, 1000):
    if n % 3 == 0 or n % 5 == 0:
        somme += n
    
print(somme)