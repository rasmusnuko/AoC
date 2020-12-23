import sys
import numpy as np
inputza = open('AoC10.txt', 'r')
# Getting numbers and preamble
''' FIRST STAR '''
numbers = [int(line.strip()) for line in inputza.readlines()]
numbers.append(0)
numbers.append(max(numbers)+3)
numbers = sorted(numbers)
ones = 0
threes = 0
for i in range(len(numbers)-1):
    if numbers[i]+1 == numbers[i+1]:
        ones += 1
    elif numbers[i]+3 == numbers[i+1]:
        threes += 1
print("First star:", ones*threes)

''' SECOND STAR '''
canReach = [[numbers[x], [number for number in numbers if 0 < number-numbers[x] <= 3]] for x in range(len(numbers))]
possibleArrangements = canReach[-1][1]
for i in reversed(range(1, len(numbers)-1)):
    possibleArrangements += canReach[i][1]
canReach[-1][1] = []