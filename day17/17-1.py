from collections import defaultdict

NEXT = {
    'd': ('d', 'r', 'l'),
    'u': ('r', 'l', 'u'),
    'l': ('d', 'l', 'u'),
    'r': ('d', 'r', 'u'),
    'X' : ('u', 'd', 'r', 'l'),
}

def v(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]):
        return False
    return True

def n(x, y, d):
    if d == 'd':
        return (x + 1, y)
    elif d == 'u':
        return (x - 1, y)
    elif d == 'r':
        return (x, y + 1)
    elif d == 'l':
        return (x, y - 1)

def c():
    return {'d': -1, 'dd': -1, 'ddd': -1, 'u': -1, 'uu': -1, 'uuu': -1, 'l': -1, 'll': -1, 'lll': -1, 'r': -1, 'rr': -1, 'rrr': -1}

f = open('input17.txt')

m = []
costs = []

for l in f:
    m.append([int(x) for x in l.strip()])
    costs.append([])
    for _ in range(len(m[-1])):
        costs[-1].append(c())

horizon = defaultdict(set)
horizon[0] = {(0, 0, 'X')}
costs[0][0]['X'] = -1

while 1:
    best = min(horizon.keys())
    x, y, d = horizon[best].pop()
    if x == len(m) - 1 and y == len(m[-1]) - 1:
        print(best)
        break
    if not horizon[best]:
        del(horizon[best])
    costs[x][y][d] = best
    for nxt in NEXT[d[0]]:
        x1, y1 = n(x, y, nxt)
        d1 = ''
        if not v(x1, y1, m):
            continue
        if d[0] == nxt:
            if len(d) > 2:
                continue
            d1 = d + nxt
        else:
            d1 = nxt
        if costs[x1][y1][d1] == -1:
            horizon[best + m[x1][y1]].add((x1, y1, d1))
