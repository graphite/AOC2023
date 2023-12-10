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


bfs = []
for shift in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    x, y = shift[0] + start[0], shift[1] + start[1]
    if transitions[maze[x][y]][shift] is None:
        continue
    bfs.append(((x, y), transitions[maze[x][y]][shift]))

n = 0
while True:
    n += 1
    current_coords = set(c[0] for c in bfs)
    if len(current_coords) != len(bfs):
        break
    new_bfs = []
    for coords, shift in bfs:
        x, y = coords[0] + shift[0], coords[1] + shift[1]
        if transitions[maze[x][y]][shift] is None:
            continue
        new_bfs.append(((x, y), transitions[maze[x][y]][shift]))
    bfs = new_bfs

print(n)
