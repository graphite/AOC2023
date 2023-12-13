f = open('input13.txt')

task = []

def find(pattern):
    rows = [int(x, base=2) for x in pattern]
    columns = []
    for i in range(len(pattern[0])):
        columns.append(int(''.join([x[i] for x in pattern]), base=2))
    r = check(rows)
    if r != 0:
        return r * 100
    r = check(rows[::-1])
    if r != 0:
        return (len(rows) - r) * 100
    r = check(columns)
    if r != 0:
        return r
    r = check(columns[::-1])
    if r != 0:
        return len(columns) - r

def check(row):
    for i in range(len(row) - 1):
        if (len(row) - i) % 2 == 1:
            continue
        for j in range((len(row)-i) // 2):
            if row[j + i] != row[len(row) - 1 - j]:
                break
        else:
            return i + (len(row) - i) // 2
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
