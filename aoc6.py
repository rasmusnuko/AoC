import numpy as np
import string
inputza = open('AoC6.txt', 'r')
# Getting credentials
allInfo = ''
for line in inputza.readlines():
    allInfo += line
info = allInfo.split("\n\n")
for x in range(len(info)):
    info[x] = info[x].split()
'''First star
allGroups = []
for group in info:
    groupUniques = []
    for person in group:
        for answer in person:
            if answer not in groupUniques:
                groupUniques.append(answer)
    allGroups.append(len(groupUniques))

print(sum(allGroups))'''
# Second star
allGroups = []
for group in info:
    groupCommons = []
    for person in group:
        for answer in person:
            check = True
            for person in group:
                if answer not in person or answer in groupCommons:
                    check = False
            if check:
                groupCommons.append(answer)
    allGroups.append(len(groupCommons))
    groupCommons = []

print(sum(allGroups))