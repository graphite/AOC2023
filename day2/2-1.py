f = open('input2.txt')

M_RED = 12
M_GREEN = 13
M_BLUE = 14

n = 0

for l in f:
    l = l.strip()
    game, rest = l.split(': ')
    game = int(game[4:])
    possible = True
    for r in rest.split('; '):
        for balls in r.split(', '):
            num, col = balls.split(' ')
            num = int(num)
            mnum = 0
            if col == 'red':
                mnum = M_RED
            elif col == 'green':
                mnum = M_GREEN
            elif col == 'blue':
                mnum = M_BLUE
            if num > mnum:
                possible = False
                break
        if not possible:
            break
    if possible:
        n += game

print(n)
