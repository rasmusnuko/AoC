import copy
import sys
inputza = open('AoC8.txt', 'r')
# Getting lines
lines = [line.strip() for line in inputza.readlines()]
# Splitting action and values
for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
    # String to int
    if lines[i][1][0] == '+':
        lines[i][1] = lines[i][1][1:]
    lines[i][1] = int(lines[i][1])

# First star
index = 0
acc = 0
visited = []
while index not in visited and index < len(lines):
    if lines[index][0] == 'nop':
        visited.append(index)
        index += 1
    elif lines[index][0] == 'acc':
        acc += lines[index][1]
        visited.append(index)
        index += 1
    elif lines[index][0] == 'jmp':
        visited.append(index)
        index += lines[index][1]
print("First star:", acc)

# Second star
loopCondition = True
altered = []
while(loopCondition):
    # Swapping a 'nop' for a 'jmp' or vise versa
    linesAltered = copy.deepcopy(lines)
    i = 0
    swapped = False
    while(not swapped):
        assert(i < len(linesAltered))
        if linesAltered[i][0] == 'jmp' and i not in altered:
            linesAltered[i][0] = "nop"
            altered.append(i)
            swapped = True
        elif linesAltered[i][0] == 'nop' and i not in altered:
            linesAltered[i][0] = "jmp"
            altered.append(i)
            swapped = True
        i += 1
    
    index = 0
    acc = 0
    visited = []
    while index not in visited and index < len(linesAltered):
        if linesAltered[index][0] == 'nop':
            visited.append(index)
            index += 1
        elif linesAltered[index][0] == 'acc':
            acc += linesAltered[index][1]
            visited.append(index)
            index += 1
        elif linesAltered[index][0] == 'jmp':
            visited.append(index)
            index += linesAltered[index][1]
    if index not in visited:
        loopCondition = False
        
print("Second star:", acc)