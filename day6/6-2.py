f = open('input6.txt')

time = int(''.join(f.readline().strip().split()[1:]))
dist = int(''.join(f.readline().strip().split()[1:]))

for i in range(time):
    if (time - i) * i > dist:
        break

print(time - 2 * (i - 1) - 1)
