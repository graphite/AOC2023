f = open('input13.txt')

P2 = set([2**x for x in range(20)])
task = []

def find(pattern):
    rows = [int(x, base=2) for x in pattern]
    columns = []
    for i in range(len(pattern[0])):
        columns.append(int(''.join([x[i] for x in pattern]), base=2))

    r1 = check(rows) or None
    r2 = check(rows[::-1]) or None
    for i in range(len(rows) - 1):
        for j in range(i + 1, len(rows)):
            if (rows[i] ^ rows[j]) in P2:
                option = [x for x in rows]
                option[i] = option[j]
                r = check(option, orig=r1)
                if r != 0:
                    r = r + (len(rows) - r) // 2
                    return r * 100
                r = check(option[::-1], orig=r2)
                if r != 0:
                    r = r + (len(rows) - r) // 2
                    return (len(rows) - r) * 100

    r1 = check(columns) or None
    r2 = check(columns[::-1]) or None
    for i in range(len(columns) - 1):
        for j in range(i + 1, len(columns)):
            if (columns[i] ^ columns[j]) in P2:
                option = [x for x in columns]
                option[i] = option[j]
                r = check(option, orig=r1)
                if r != 0:
                    r = r + (len(columns) - r) // 2
                    return r
                r = check(option[::-1], orig=r2)
                if r != 0:
                    r = r + (len(columns) - r) // 2
                    return len(columns) - r

def check(row, orig=None):
    for i in range(len(row) - 1):
        if (len(row) - i) % 2 == 1 or i == orig:
            continue
        for j in range((len(row)-i) // 2):
            if row[j + i] != row[len(row) - 1 - j]:
                break
        else:
            return i
    return 0

n = 0

for l in f:
    l = l.strip()
    if not l:
        n += find(task)
        task = []
    else:
        task.append(l.replace('.', '1').replace('#', '0'))

n += find(task)

print(n)
