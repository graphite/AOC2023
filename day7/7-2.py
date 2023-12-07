from collections import defaultdict

f = open('input7.txt')

SCORES = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def get_value(hand):
    v = 0
    cards = defaultdict(int)
    for c in hand:
        cards[c] += 1
        v = v * 14 + SCORES[c]
    if 'J' in cards:
        if len(cards) > 1:
            best = sorted(cards.keys(), key=lambda x: cards[x] if x != 'J' else 0)[-1]
            cards[best] += cards['J']
            del(cards['J'])
    if max(cards.values()) == 5:
        v += 7000000
    elif max(cards.values()) == 4:
        v += 6000000
    elif len(cards) == 2:
        v += 5000000
    elif max(cards.values()) == 3:
        v += 4000000
    elif len(cards) == 3:
        v += 3000000
    elif max(cards.values()) == 2:
        v += 2000000
    return v

hands = []

for l in f:
    hand, bid = l.strip().split()
    bid = int(bid)
    hands.append((get_value(hand), bid))

hands.sort(key=lambda x: x[0])
n = 0

for i in range(len(hands)):
    n += (i + 1) * hands[i][1]

print(n)
