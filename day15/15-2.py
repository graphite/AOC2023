f = open('input15.txt')

l = f.read().strip()

def h(s):
    r = 0
    for c in s:
        r += ord(c)
        r *= 17
        r %= 256
    return r

boxes = []
for _ in range(256):
    boxes.append([])

for s in l.split(','):
    if s[-1] == '-':
        lens = s[:-1]
        box = h(lens)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == lens:
                boxes[box].pop(i)
                break
    else:
        lens, focus = s.split('=')
        focus = int(focus)
        box = h(lens)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == lens:
                boxes[box][i][1] = focus
                break
        else:
            boxes[box].append([lens, focus])

n = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        n += (i + 1) * (j + 1) * boxes[i][j][1]

print(n)
