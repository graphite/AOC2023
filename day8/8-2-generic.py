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
shifts_set = set()
for n in nodes:
    pos = n
    i = 0
    while True:
        step = steps[i % len(steps)]
        i += 1
        pos = nodes[pos][0 if step == 'L' else 1]
        if pos[-1] == 'Z':
            next_exits[n] = i
            shifts_set.add(i - i % len(steps))
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
    # There is a corner case of shift == 0 here, i.e. all nodes have exits within next block,
    # but the closest differs. A bitmask of exits for the next block for each node can solve this.
    shift = max(exits) - max(exits) % len(steps)
    i += shift
    positions = [transitions[x][shift] for x in positions]
    exits = set(next_exits[x] for x in positions)
    if i == 13289612809129:
        print(positions)
        print(exits)
        exit()
    new_t = datetime.datetime.now()
    if (new_t - t).seconds >= 10:
        t = new_t
        print('[{} seconds] Current step: {}, {}/s'.format((t - start_t).seconds, i, i / (t - start_t).seconds))

for x in exits:
    i += x
    break

print(i)
