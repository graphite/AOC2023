f = open('input3.txt')

m = []
n = []
s = []

for l in f:
    l = l.strip()
    m.append([])
    n.append([])
    for c in l:
        m[-1].append(c)
        n[-1].append(' ')
        if c == '*':
            s.append((len(m) - 1, len(m[-1]) - 1))

def nbrs(x, y):
    return (
        (x-1,y-1),
        (x,y-1),
        (x+1,y-1),
        (x-1,y),
        (x+1,y),
        (x-1,y+1),
        (x,y+1),
        (x+1,y+1),
    )

def v(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[-1]):
        return False
    return True

def copyr(x, y, m, n):
    while v(x, y, m) and m[x][y].isdigit():
        n[x][y] = m[x][y]
        y += 1

def copyl(x, y, m, n):
    while v(x, y, m) and m[x][y].isdigit():
        n[x][y] = m[x][y]
        y -= 1

def getnum(x, y, nbr, n):
    num = ''
    if nbr == 'l':
        y -= 1
    elif nbr == 'r':
        y += 1
    elif nbr[0] == 't':
        x -= 1
        if nbr == 'tl':
            y -= 1
        elif nbr == 'tr':
            y += 1
    elif nbr[0] == 'b':
        x += 1
        if nbr == 'bl':
            y -= 1
        elif nbr == 'br':
            y += 1

    while v(x, y, n) and n[x][y].isdigit():
        y -= 1

    y += 1
    while v(x, y, n) and n[x][y].isdigit():
        num += n[x][y]
        y += 1
    print(nbr, num, x, y)
    return int(num)

r = 0
for x, y in s:
    for nx, ny in nbrs(x, y):
        if not v(nx, ny, m):
            continue
        if not m[nx][ny].isdigit():
            continue
        copyr(nx, ny, m, n)
        copyl(nx, ny, m, n)
    nums = []
    if n[x][y-1].isdigit():
        nums.append('l')
    if n[x][y+1].isdigit():
        nums.append('r')
    if n[x-1][y-1] == ' ':
        if n[x-1][y].isdigit():
            nums.append('t')
        elif n[x-1][y+1].isdigit():
            nums.append('tr')
    else:
        nums.append('tl')
        if n[x-1][y] == ' ' and n[x-1][y+1].isdigit():
            nums.append('tr')
    if n[x+1][y-1] == ' ':
        if n[x+1][y].isdigit():
            nums.append('b')
        elif n[x+1][y+1].isdigit():
            nums.append('br')
    else:
        nums.append('bl')
        if n[x+1][y] == ' ' and n[x+1][y+1].isdigit():
            nums.append('br')
    if len(nums) == 2:
        r += getnum(x, y, nums[0], n) * getnum(x, y, nums[1], n)

print(r)
