f = open('input4.txt')

cards = [1] * 212
i = 0
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
    n += cards[i]
    while w > 0:
        cards[i + w] += cards[i]
        w -= 1
    i += 1

print(n)
