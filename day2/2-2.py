f = open('input2.txt')

n = 0

for l in f:
    l = l.strip()
    _, rest = l.split(': ')
    nums = {'red': 0, 'green': 0, 'blue': 0}
    for r in rest.split('; '):
        for balls in r.split(', '):
            num, col = balls.split(' ')
            num = int(num)
            nums[col] = max(nums[col], num)
    n += nums['red'] * nums['green'] * nums['blue']

print(n)
