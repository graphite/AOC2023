f = open('input16.txt')

tiles = []

for l in f:
    tiles.append(l.strip())

visited = set()
visited_dir = set()
# Directions 0 up, 1 right, 2 down, 3 left

def v(x, y, tiles):
    if x < 0 or y < 0 or x >= len(tiles) or y >= len(tiles[0]):
        return False
    return True

def next_tile(x, y, d):
    return ((x - 1, y, d), (x, y + 1, d), (x + 1, y, d), (x, y - 1, d))[d]

# Entering at (0, 0) going right
beams = [(0, 0, 1)]
while beams:
    beam = beams.pop()
    visited.add((beam[0], beam[1]))
    visited_dir.add(beam)
    x, y, d = beam
    new_tiles = []
    cur = tiles[x][y]
    if cur == '.':        
        new_tiles.append(next_tile(x, y, d))
    elif cur == '|':
        if d == 1 or d == 3:
            new_tiles.append(next_tile(x, y, 0))
            new_tiles.append(next_tile(x, y, 2))
        else:
            new_tiles.append(next_tile(x, y, d))
    elif cur == '-':
        if d == 0 or d == 2:
            new_tiles.append(next_tile(x, y, 1))
            new_tiles.append(next_tile(x, y, 3))
        else:
            new_tiles.append(next_tile(x, y, d))
    elif cur == '/':
        d = (1, 0, 3, 2)[d]
        new_tiles.append(next_tile(x, y, d))
    elif cur == '\\':
        d = (3, 2, 1, 0)[d]
        new_tiles.append(next_tile(x, y, d))

    for tile in new_tiles:
        if tile in visited_dir or not v(tile[0], tile[1], tiles):
            continue
        beams.append(tile)

print(len(visited))
