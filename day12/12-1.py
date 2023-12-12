f = open('input12.txt')

n = 0

CACHE = {}

def permutations(row, nums):
    #print(row, nums)
    row = row.strip('.')
    #print(CACHE)
    if not nums:
        if '#' in row:
            return 0
        else:
            return 1
    if len(nums) == 1:
        if nums[0] == len(row):
            if '.' in row:
                CACHE[(row, nums)] = 0
                return 0
            else:
                CACHE[(row, nums)] = 1
                return 1
    if (row, nums) in CACHE:
        return CACHE[(row, nums)]
    n = nums[0]
    br = row.find('#')
    if br == -1:
        br = len(row)
    for i in range(len(row) - n + 1):
        if i > br:
            CACHE[(row, nums)] = 0
            return 0
        if '.' not in row[i:i+n]:
            if i + n < len(row) and row[i + n] != '#':
                break
            if i + n == len(row):
                break
    else:
        CACHE[(row, nums)] = 0
        return 0
    if i + n == len(row):
        if len(nums) > 1:
            CACHE[(row, nums)] = 0
            return 0
        else:
            CACHE[(row, nums)] = 1
            return 1
    CACHE[(row, nums)] = permutations(row[i + n + 1:], nums[1:]) + (permutations(row[i + 1:], nums) if row[i] != '#' else 0)
    return CACHE[(row, nums)]

for l in f:
    l = l.strip()
    row, nums = l.split()
    nums = tuple(int(x) for x in nums.split(','))
    n += permutations(row, nums)
    #print(n)
    #print(CACHE)
    #break

print(n)
