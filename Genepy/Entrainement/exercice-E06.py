# La suite de Fibonacci

# Ce programme fonctionne en local sur mon pc
# Il est cependant trop lent pour Hackinscience
 
# cette fonction calcule le terme de rang n de la suite de fibonacci

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
# cette fonction calcule les n premiers termes de la suite de fibonacci
    
def fibonacci(n):
    a_list = []
    for i in range(1, n+1):
        a_list.append(fibo(i))
    return a_list

# simplement des tests

print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(31))