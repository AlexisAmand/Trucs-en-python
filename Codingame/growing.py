# Puzzle : Next Growing Number

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
is_growing = False

while is_growing == False:
    n += 1
    is_growing = True

    for i in range(len(str(n)) - 1):
        if str(n)[i] > str(n)[i + 1]:
            is_growing = False
            break

print(n)