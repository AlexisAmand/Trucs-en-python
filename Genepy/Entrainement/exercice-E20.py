# Trois entiers consécutifs

def find_consecutive_sum(n):
    # On cherche des triplets (a, b, c) consécutifs
    for i in range(1, n // 3):  # Limité à n // 3 car trois nombres consécutifs doivent être inférieurs à n
        a = i
        b = a + 1
        c = b + 1
        if a + b + c == n:
            return a, b, c
    return None



