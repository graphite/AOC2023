f = open('input1.txt')

n = 0

for l in f:
    d = ''
    for c in l:
        if c.isdigit():
            d = c
            break
    for i in range(len(l) - 1, -1, -1):
        if l[i].isdigit():
            d += l[i]
            break
    n += int(d)

print(n)
