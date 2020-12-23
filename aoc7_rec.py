import numpy as np
import string
import sys
inputza = open('AoC7.txt', 'r')
sys.setrecursionlimit(3000)

def getWeigth(info, indecies, name, knownBags):
    # Found bag we know
    for known in knownBags:
        if name == known[0]:
            # Return weight of bag, if the bag is known
            return known[1]

    ### Found new bag
    # Finding it's index 
    index = 0
    weight = 1
    for entry in indecies:
        if name == entry[0]:
            index = int(entry[1])
    # Going through the found bag
    # summing all bags inside it recursively 
    for content in info[index][1]:
        weight += content[0] * getWeigth(info, indecies, content[2:].strip(), knownBags)
    knownBags.append((name, weight))
    return weight

if __name__ == '__main__':
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
    def recursion(info, indecies, name, knownBags):
        for known in knownBags:
            if name == known[0]:
                # Return 'weight' of bag, if the 'weight' is known
                return known[1]

    for x in range(len(info)):
        info[x][1] = info[x][1].split(",")
        for y in range(len(info[x][1])):
            info[x][1][y] = info[x][1][y].strip().strip(" bags.")

    # Paiting indecies and names
    indecies = [(info[x][0], x) for x in range(len(info))]

    # Finding 'empty bags' (Doens't have any other bags in them)
    knownBags = [(x[0], 1) for x in info if x[1][0] == 'no other']
    print("Second star:", getWeigth(info, indecies, "shiny gold", knownBags))
    print("hello")