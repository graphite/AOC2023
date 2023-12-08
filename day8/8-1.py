f = open('input8.txt')

steps = f.readline().strip()
f.readline()

nodes = {}

for l in f:
    n, rest = l.strip().split(' = ')
    left, right = rest[1:-1].split(', ')
    nodes[n] = (left, right)

n = 'AAA'
i = 0

while n != 'ZZZ':
    s = steps[i % len(steps)]
    n = nodes[n][0 if s == 'L' else 1]
    i += 1

print(i)
