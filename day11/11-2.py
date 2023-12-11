f = open('input11.txt')

universe = []
galaxies = []
i = 0

for l in f:
    universe.append(l.strip())
    for j in range(len(universe[-1])):
        if universe[-1][j] == '#':
            galaxies.append((i, j))
    i += 1

expanded_rows = set(range(len(universe)))
expanded_cols = set(range(len(universe[-1])))

for x, y in galaxies:
    try:
        expanded_rows.remove(x)
    except:
        pass
    try:
        expanded_cols.remove(y)
    except:
        pass

n = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        n += abs(x1 - x2) + abs(y1 - y2)
        for r in expanded_rows:
            if r > min(x1, x2) and r < max(x1, x2):
                n += 1000000 - 1
        for c in expanded_cols:
            if c > min(y1, y2) and c < max(y1, y2):
                n += 1000000 - 1
        
print(n)
