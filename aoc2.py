inputza = open('AoC2.txt', 'r')
strings = [line.split(":") for line in inputza.readlines()]
ranges = [(int(strings[x][0].split("-")[0]), int(strings[x][0].split("-")[1].split(" ")[0])) for x in range(len(strings))]
letters = [strings[x][0][-1] for x in range(len(strings))]
passphrases = [strings[x][1].strip() for x in range(len(strings))]
''' 1. Star
for i in range(len(strings)):
    letterCount = 0
    for letter in passphrases[i]:
        if letter == letters[i]:
            letterCount += 1
    if letterCount in range(ranges[i][0], ranges[i][1]+1):
        valid += 1
        '''
        
#2. Star
valid = 0
for i in range(len(strings)):
    nr1Index = passphrases[i][(ranges[i][0]-1)] == letters[i]
    nr2Index = passphrases[i][(ranges[i][1]-1)] == letters[i]
    print(nr1Index, nr2Index)
    if nr1Index != nr2Index:
        valid += 1
print(valid)