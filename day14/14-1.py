f = open('input14.txt')

rocks = []

for l in f:
    rocks.append(l.strip())

n = 0
for j in range(len(rocks[0])):
    base = len(rocks)
    for i in range(len(rocks)):
        if rocks[i][j] == '#':
            base = len(rocks) - i - 1
        if rocks[i][j] == 'O':
            n += base
            base -= 1

print(n)
