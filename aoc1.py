numbers = open('AoC1.txt', 'r')
result = [line.split('\n') for line in numbers.readlines()]
result = [int(result[x][0]) for x in range(len(result))]
result = sorted(result)
print(result)
x = 0
y = 0
z = 0
for i in range(len(result)):
    for j in reversed(range(len(result))):
        for k in reversed(range(len(result))):
            if result[i] + result[j] + result[k] == 2020:
                x = result[i]
                y = result[j]
                z = result[k]
print(x*y*z)