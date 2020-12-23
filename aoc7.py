import numpy as np
import string
import sys
inputza = open('AoC7.txt', 'r')
# Getting credentials
info = [line for line in inputza.readlines()]
info = [line.strip().split(" bags contain ") for line in info]
'''First star
validBags = ["shiny gold"]
new_bags_added = True
while(new_bags_added):
    new_bags_added = False
    for rules in info:
        for bag in validBags:
            if bag in rules[1]:
                if rules[0] not in validBags:
                    validBags.append(rules[0])
                    new_bags_added = True
print("First star:", len(validBags)-1)'''
# Second star
# Pairing bags and their contents
for x in range(len(info)):
    info[x][1] = info[x][1].split(",")
    for y in range(len(info[x][1])):
        info[x][1][y] = info[x][1][y].strip().strip(" bags.")

# Pairing names and indecies
indecies = [(info[x][0], x) for x in range(len(info))]

# Finding 'empty bags' (Doens't have any other bags in them)
knownBags = [(bag[0], 1) for bag in info if bag[1][0] == 'no other']
strippedInfo = []
for x in range(len(info)):
    weight = 0
    strippedInfo.append((info[x][0], [y[2:] for y in info[x][1]]))
    if any([bags in [knownBags[x][0] for x in range(len(knownBags))] for bags in strippedInfo[x]]):
        for bag in [knownBags[x][0] for x in range(len(knownBags))]:
            if bag in strippedInfo[x]:
                weight += int(bag[1])
        knownBags.append((info[x][0], weight))