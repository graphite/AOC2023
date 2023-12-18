from collections import defaultdict

f = open('input18.txt')

def count(cur, ranges, h_lines=None):
    ys = []
    for x, y, x1, d in ranges:
        if cur < x:
            break
        if cur >= x and cur <= x1:
            ys.append((y, d))
    ys = sorted(ys)
    ins = True
    y, d = ys[0]
    r = [[y, y]]
    for y1, d1 in ys[1:]:
        if d1 == d:
            r[-1][1] = y1
        else:
            if ins:
                r[-1][1] = y1
            else:
                r.append([y1, y1])
            ins = not ins
        y, d = y1, d1

    if h_lines:
        for x, y in h_lines:
            for i in range(len(r)):
                if r[i][1] == x:
                    r = r[:i] + [[r[i][0], r[i+1][1]]] + r[i+2:]
                    break
    return sum(y - x + 1 for x, y in r)


ranges = []
h_lines = defaultdict(list)
corners = set()

x = y = 0

for l in f:
    _, _, data = l.strip().split()
    d = data[-2]
    n = int(data[2:-2], 16)
    corners.add(x)
    if d == '1':
        ranges.append((x, y, x + n, 'd'))
        x += n
    elif d == '3':
        ranges.append((x - n, y, x, 'u'))
        x -= n
    elif d == '0':
        h_lines[x].append((y, y + n))
        y += n
    elif d == '2':
        h_lines[x].append((y - n, y))
        y -= n

n = 0
ranges = sorted(ranges)
corners = sorted(corners)
for i in range(len(corners)):
    cur = corners[i]
    n += count(cur, ranges, h_lines[cur])


    if i + 1 == len(corners):
        continue

    if corners[i+1] == cur + 1:
        continue

    n += count(cur + 1, ranges) * (corners[i+1] - cur - 1)

print(n)
