# Puzzle : Euclid's Algorithm

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def euclide(a, b):
    if b == 0:
        return a
    else:
        print(f"{a}={b}*{a // b}+{a % b}")
        euclide(b, a % b)



def euclide2(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

        

euclide(a, b)
print(f"GCD({a},{b})={euclide2(a,b)}")