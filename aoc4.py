import numpy as np
from collections import deque
inputza = open('AoC4.txt', 'r')
# Getting credentials
allInfo = ''
for line in inputza.readlines():
    allInfo += line
info = allInfo.split("\n\n")
info = [line.split() for line in info]
# Strings to tuples
for i in range(len(info)):
    for j in range(len(info[i])):
        info[i][j] = (info[i][j].split(":")[0], info[i][j].split(":")[1])
## First star
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
currentPassport = []
valid = 0
for passport in info:
    currentPassportCreds = [passport[x][0] for x in range(len(passport))]
    if len(currentPassportCreds) > 6:
        if all([req in currentPassportCreds for req in required]):
            valid += 1
print(valid)
