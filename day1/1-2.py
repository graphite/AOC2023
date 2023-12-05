f = open('input1.txt')

digs = {'one': '1', '1': '1', 'two': '2', '2': '2', 'three': '3', '3': '3', 'four': '4', '4': '4', 'five': '5', '5': '5', 'six': '6', '6': '6', 'seven': '7', '7': '7', 'eight': '8', '8': '8', 'nine': '9', '9': '9'}

n = 0

for l in f:
    d = ['0', '0']
    minpos = len(l)
    maxpos = -1
    for dig in digs.keys():
        pos = l.find(dig)
        if pos == -1:
            continue
        if pos < minpos:
            minpos = pos
            d[0] = digs[dig]
        pos = l.rfind(dig)
        if pos > maxpos:
            maxpos = pos
            d[1] = digs[dig]

    n += int(''.join(d))

print(n)
