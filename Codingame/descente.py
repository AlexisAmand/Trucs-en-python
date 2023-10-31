# puzzle : Descente

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

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
