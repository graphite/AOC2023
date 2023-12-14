from hashlib import md5

f = open('input14.txt')

rocks = []

for l in f:
    rocks.append([c for c in l.strip()])

new_rocks = [['.'] * len(rocks) for _ in range(len(rocks))]

known = {}

n = 1
while 1:
    for _ in range(4):
        for j in range(len(rocks)):
            base = 0
            for i in range(len(rocks)):
                if rocks[i][j] == '#':
                    new_rocks[j][len(rocks) - i - 1] = '#'
                    base = i + 1
                elif rocks[i][j] == 'O':
                    new_rocks[j][len(rocks) - i - 1] = '.'
                    new_rocks[j][len(rocks) - base - 1] = 'O'
                    base += 1
                else:
                    new_rocks[j][len(rocks) - i - 1] = '.'
        new_rocks, rocks = rocks, new_rocks
    load = 0
    for j in range(len(rocks)):
        base = len(rocks)
        for i in range(len(rocks)):
            if rocks[i][j] == 'O':
                load += len(rocks) - i
    h = md5()
    for l in rocks:
        h.update(''.join(l))
    if h.digest() in known:
        start = known[h.digest()][0]
        cycle = n - start
        target = start + ((1000000000 - n) % cycle)
        break
    known[h.digest()] = (n, load)
    n += 1

for n, load in known.values():
    if n == target:
        print(load)
        break
