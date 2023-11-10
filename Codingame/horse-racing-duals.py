# Puzzle : Horse Racing Duals

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

P = dict()

n = int(input())
for i in range(n):
    P[i] = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

D = abs(P[0] - P[1])

for i in range (0, n-1):
    for k in range(0, n):
        if i == k:
            continue
        Dtemp = abs(P[i] - P[k])
        if Dtemp < D:
            D = Dtemp

print(f"{D}")