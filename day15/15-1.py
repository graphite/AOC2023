f = open('input15.txt')

l = f.read().strip()

n = 0
for h in l.split(','):
    r = 0
    for c in h:
        r += ord(c)
        r *= 17
        r %= 256
    n += r

print(n)
