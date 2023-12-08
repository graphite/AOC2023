import datetime

f = open('input8.txt')

steps = f.readline().strip()
f.readline()

nodes = {}
starts = []

print('Reading nodes...')
for l in f:
    n, rest = l.strip().split(' = ')
    left, right = rest[1:-1].split(', ')
    nodes[n] = (left, right)
    if n[-1] == 'A':
        starts.append(n)

print('Calculating closest exits...')
next_exits = {}
block_exits = {}
shifts_set = set()
for n in nodes:
    pos = n
    i = 0
    block_exits[n] = set()
    while i < len(steps) or n not in next_exits:
        if pos[-1] == 'Z':
            if n not in next_exits:
                next_exits[n] = i
                shifts_set.add(i - i % len(steps))
            if i < len(steps):
                block_exits[n].add(i)
        step = steps[i % len(steps)]
        pos = nodes[pos][0 if step == 'L' else 1]
        i += 1
        if i > len(steps) * len(nodes):
            # This node is a dead end, if we reach it the program will fail
            # as there is no solution.
            break

print('Calculating transitions table...')
transitions = {}
for n in nodes:
    pos = n
    i = 0
    transitions[n] = {}
    for i in range(max(shifts_set) + 1):
        step = steps[i % len(steps)]
        pos = nodes[pos][0 if step == 'L' else 1]
        if i + 1 in shifts_set:
            transitions[n][i + 1] = pos

print('Solving...')
exits = set(next_exits[x] for x in starts)
positions = starts
start_t = t = datetime.datetime.now()
i = 0
while len(exits) != 1:
    shift = max(exits) - max(exits) % len(steps)
    if shift == 0:
        current_block_exits = block_exits[positions[0]]
        for pos in positions[1:]:
            current_block_exits = current_block_exits.intersection(block_exits[pos])
        if current_block_exits:
            exits = set(min(current_block_exits))
            break
        shift = len(steps)
    i += shift
    positions = [transitions[x][shift] for x in positions]
    exits = set(next_exits[x] for x in positions)
    new_t = datetime.datetime.now()
    if (new_t - t).seconds >= 10:
        t = new_t
        print('[{} seconds] Current step: {}, {}/s'.format((t - start_t).seconds, i, i / (t - start_t).seconds))

for x in exits:
    i += x
    break

print('Result:', i)
