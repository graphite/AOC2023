from collections import defaultdict

NEXT = {
    'd': ('r', 'l'),
    'u': ('r', 'l'),
    'l': ('d', 'u'),
    'r': ('d', 'u'),
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
    if costs[x][y][d] != -1 and costs[x][y][d] <= best:
        continue
    costs[x][y][d] = best
    for nxt in NEXT[d]:
        c = 0
        x1, y1 = x, y
        for _ in range(3):
            x1, y1 = n(x1, y1, nxt)
            if not v(x1, y1, m):
                break
            c += m[x1][y1]
        for _ in range(7):
            x1, y1 = n(x1, y1, nxt)
            if not v(x1, y1, m):
                break
            c += m[x1][y1]
            if costs[x1][y1][nxt] == -1 or costs[x1][y1][nxt] > c + best:
                horizon[best + c].add((x1, y1, nxt))
