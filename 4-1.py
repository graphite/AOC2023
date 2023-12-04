f = open('input4.txt')

n = 0
for l in f:
    l = l.strip()
    _, rest = l.split(': ')
    card, nums = rest.split('|')
    card = set(int(x) for x in card.split())
    w = 0
    for num in nums.split():
        if int(num) in card:
            w += 1
    if w:
        n += 2**(w-1)

print(n)
