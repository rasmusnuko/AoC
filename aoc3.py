import numpy as np
from collections import deque
inputza = open('AoC3.txt', 'r')
slope = [line.strip() for line in inputza.readlines()]
treeEncounter = 0
column = 1
for row in range(2, len(slope), 2):
    print(row)
    if slope[row][column%len(slope[0])] == '#':
        treeEncounter += 1
    column += 1

print(treeEncounter)
print(230*104*83*98*49)