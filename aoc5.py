import numpy as np
from collections import deque
inputza = open('AoC5.txt', 'r')
# Getting credentials
info = [line.strip() for line in inputza.readlines()]
seatIDs = []
for passenger in info:
    row = 0
    column = 0
    if passenger[0] == 'B':
        row += 64
    if passenger[1] == 'B':
        row += 32
    if passenger[2] == 'B':
        row += 16
    if passenger[3] == 'B':
        row += 8
    if passenger[4] == 'B':
        row += 4
    if passenger[5] == 'B':
        row += 2
    if passenger[6] == 'B':
        row += 1
    if passenger[7] == 'R':
        column += 4
    if passenger[8] == 'R':
        column += 2
    if passenger[9] == 'R':
        column += 1
    seatIDs.append((row*8)+column)
print("First star:", max(seatIDs))
    
#Second star
minID = min(seatIDs)
maxID = max(seatIDs)
for x in range(minID, maxID):
    if x not in seatIDs:
        print("Second star:", x)