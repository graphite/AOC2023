f = open('input6.txt')

times = [int(x) for x in f.readline().strip().split()[1:]]
dists = [int(x) for x in f.readline().strip().split()[1:]]

n = 1

for i in range(len(times)):
    for j in range(times[i]):
        if (times[i] - j) * j > dists[i]:
            break
    n *= times[i] - 2 * (j - 1) - 1

print(n)
