def n(x, y, d, l=1):
    if d == 'U':
        return (x - l, y)
    elif d == 'D':
        return (x + l, y)
    elif d == 'R':
        return (x, y + l)
    elif d == 'L':
        return (x, y - l)

def v(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]):
        return False
    return True

f = open('input18.txt')

digs = []

x = y = maxx = minx = maxy = miny = 0
for line in f:
    d, l, _ = line.strip().split()
    l = int(l)
    digs.append((d, l))
    x, y = n(x, y, d, l)
    maxx, minx = max(maxx, x), min(minx, x)
    maxy, miny = max(maxy, y), min(miny, y)

x, y = abs(minx) + 1, abs(miny) + 1

m = [['.'] * (3 + maxy - miny) for _ in range((3 + maxx - minx))]

m[x][y] = '#'

for d, l in digs:
    for _ in range(l):
        x, y = n(x, y, d)
        m[x][y] = '#'

h = set([(0,0)])
while h:
    x, y = h.pop()
    m[x][y] = ' '
    for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if v(x1, y1, m) and m[x1][y1] == '.':
            h.add((x1, y1))

r = 0
for l in m:
    r += l.count('#') + l.count('.')
print(r)
