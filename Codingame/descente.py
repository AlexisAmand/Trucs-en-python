# Puzzle : Descente

import sys
import math

mountains = list()

# game loop
while True:

    mountains.clear()

    for i in range(8):
        mountain_height = int(input())  
        mountains.append(mountain_height)

    top_max = mountains[0]
    max_index = 0

    for x in range(8):
        if mountains[x] > top_max:
            top_max = mountains[x]
            max_index = x
   
    # The index of the mountain to fire on.
    print(max_index)
