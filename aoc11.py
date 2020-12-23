import copy
inputza = open('AoC11.txt', 'r')
''' FIRST STAR '''
#### Updates the tile located at area[row][column]
changedState = True
def updateTile(previousArea, area, row, column):
    changedState = False
    # Empty seats
    if previousArea[row][column] == 'L':
        emptyAround = True
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if not x == y == 0:
                    if previousArea[x][y] == '#':
                        emptyAround = False
        if emptyAround:
            area[row][column] = '#'
            changedState = True
    # Occupied seats
    elif previousArea[row][column] == '#':
        occupiedCount = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if not x == y == 0:
                    if previousArea[x][y] == '#':
                        occupiedCount += 1
        if occupiedCount > 3:
            area[row][column] = 'L'
            changedState = True

##### Main
area = [[char for char in line.strip()] for line in inputza.readlines()]
previousArea = []
# Update area until it's stable
while(changedState):
    changedState = False
    previousArea = copy.deepcopy(area)
    for x in range(len(area)):
        for y in range(len(area[x])):
            updateTile(previousArea, area, x, y)


# Count occupied seats when area is stable
totalOccupiedSeats = 0
for line in area:
    for tile in line:
        if tile == '#':
            totalOccupiedSeats += 1

print("First star:", totalOccupiedSeats)