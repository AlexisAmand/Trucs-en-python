# puzzle : Temperatures

import sys
import math

# liste des temperatures
t = list()

max = 6000
result = 0 

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a température expressed as an integer ranging from -273 to 5526
    t.append(int(i))

# si il n'y pas de températures dans la listea

if n == 0:
    max = 0

# sinon, compare chaque température à la valeur max
# si la température est < à max, on met la température dans max

else:
    for temperature in t:
        if abs(temperature) <= max:
            if temperature == -max:
                continue
            else:
                result = temperature
            max = abs(temperature)
        
print(result)