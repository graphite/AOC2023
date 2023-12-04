f = open('input3.txt')

m = []
n = []
s = []

for l in f:
    l = l.strip()
    m.append([])
    n.append([])
    for c in l:
        m[-1].append(c)
        n[-1].append(' ')
        if c != '.' and not c.isdigit():
            s.append((len(m) - 1, len(m[-1]) - 1))

def nbrs(x, y):
    return (
        (x-1,y-1),
        (x,y-1),
        (x+1,y-1),
        (x-1,y),
        (x+1,y),
        (x-1,y+1),
        (x,y+1),
        (x+1,y+1),
    )

def v(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[-1]):
        return False
    return True

def copyr(x, y, m, n):
    while v(x, y, m) and m[x][y].isdigit():
        n[x][y] = m[x][y]
        y += 1

def copyl(x, y, m, n):
    while v(x, y, m) and m[x][y].isdigit():
        n[x][y] = m[x][y]
        y -= 1

for x, y in s:
    for nx, ny in nbrs(x, y):
        if not v(nx, ny, m):
            continue
        if not m[nx][ny].isdigit():
            continue
        copyr(nx, ny, m, n)
        copyl(nx, ny, m, n)

r = 0
for l in n:
    for num in ''.join(l).split():
        r += int(num)

print(r)
