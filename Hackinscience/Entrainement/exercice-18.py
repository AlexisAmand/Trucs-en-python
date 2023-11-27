# La plus longue séquence de Collatz

def collatz_length(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return count
        
         
# test avec n = 10
print(f"{collatz_length(10)}\n")

# test avec n = 25
print(f"{collatz_length(25)}\n")

# test avec n = 52
print(f"{collatz_length(52)}\n")