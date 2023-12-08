f = open('input8.txt')

steps = f.readline().strip()
f.readline()

nodes = {}
starts = []

for l in f:
    n, rest = l.strip().split(' = ')
    left, right = rest[1:-1].split(', ')
    nodes[n] = (left, right)
    if n[-1] == 'A':
        starts.append(n)

shifts = []
for start in starts:
    i = 0
    pos = start
    while pos[-1] != 'Z':
        step = steps[i % len(steps)]
        i += 1
        pos = nodes[pos][0 if step == 'L' else 1]
    shifts.append(i)

def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

n = 1
for s in shifts:
    n = LCM(n, s)

print(n)
