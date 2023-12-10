f = open('input10.txt')

maze = []
start = []

# Map from into to
transitions = {
    '.': {
        (0, 1): None, (0, -1): None, (1, 0): None, (-1, 0): None,
    },
    '|': {
        (0, 1): None, (0, -1): None, (1, 0): (1, 0), (-1, 0): (-1, 0),
    },
    '-': {
        (0, 1): (0, 1), (0, -1): (0, -1), (1, 0): None, (-1, 0): None,
    },
    'L': {
        (0, 1): None, (0, -1): (-1, 0), (1, 0): (0, 1), (-1, 0): None,
    },
    'J': {
        (0, 1): (-1, 0), (0, -1): None, (1, 0): (0, -1), (-1, 0): None,
    },
    '7': {
        (0, 1): (1, 0), (0, -1): None, (1, 0): None, (-1, 0): (0, -1),
    },
    'F': {
        (0, 1): None, (0, -1): (1, 0), (1, 0): None, (-1, 0): (0, 1),
    },
}

for l in f:
    maze.append(l.strip())
    s = l.find('S')
    if s != -1:
        start = [len(maze) - 1, s]

def v(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[-1]):
        return False
    return True

def nbrs(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def print_maze(maze):
    print('\n'.join(''.join(x) for x in maze))

bfs = []
loop = []
for shift in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    x, y = shift[0] + start[0], shift[1] + start[1]
    if transitions[maze[x][y]][shift] is None:
        continue
    bfs.append(((x, y), transitions[maze[x][y]][shift]))
    loop.append([(x, y)])

# Assuming no dead end loops and only two valid starting points.
if len(loop) != 2:
    print('No can do')
    exit()

while True:
    current_coords = set(c[0] for c in bfs)
    if len(current_coords) != len(bfs):
        break
    for i in range(len(bfs)):
        coords, shift = bfs[i]
        x, y = coords[0] + shift[0], coords[1] + shift[1]
        bfs[i]=((x, y), transitions[maze[x][y]][shift])
        loop[i].append((x, y))

loop = [(start[0], start[1])] + loop[0] + loop[1][-2::-1] + [(start[0], start[1])]

# Expand! Add extra line at the end to simplify handling later
mazeX2 = []
for _ in range(len(maze) * 2):
    mazeX2.append(['.'] * (len(maze[0]) * 2))

for i in range(len(loop) - 1):
    x, y = loop[i][0], loop[i][1]
    x1, y1 = loop[i+1][0], loop[i+1][1]
    dx, dy = x1 - x, y1 - y
    mazeX2[x * 2][y * 2] = 'X'
    mazeX2[x * 2 + dx][y * 2 + dy] = 'X'

print_maze(mazeX2)

horizon = set([(0, 0)])
while horizon:
    for x, y in horizon:
        break
    horizon.remove((x,y))
    mazeX2[x][y] = ' '
    for xn, yn in nbrs(x, y):
        if v(xn, yn, mazeX2) and mazeX2[xn][yn] == '.':
            horizon.add((xn, yn))

print_maze(mazeX2)

n = 0
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if mazeX2[x * 2][y * 2] == '.':
            n += 1

print(n)
