import sys
inputza = open('AoC9.txt', 'r')
# Getting numbers and preamble
''' FIRST STAR '''
numbers = [int(line.strip()) for line in inputza.readlines()]
start = 0
stop = 25
found = True
while(found):
    found = False
    for i in range(start, stop):
        for j in range(start, stop):
            if i != j:
                if numbers[i] + numbers[j] == numbers[stop]:
                    found = True
                    start += 1
                    stop += 1
                    break
invalidNumber = numbers[stop]
print("First star:", invalidNumber)

''' SECOND STAR '''
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            if sum(numbers[i:j]) == invalidNumber:
                print("Second star:", min(numbers[i:j])+max(numbers[i:j]))
