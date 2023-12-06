f = open('input6.txt')

time = int(''.join(f.readline().strip().split()[1:]))
dist = int(''.join(f.readline().strip().split()[1:]))

# Slow solution
# for i in range(time):
#    if (time - i) * i > dist:
#        break

i, j = 0, time

while j - i > 1:
    n = (i + j) // 2
    if (time - n) * n > dist:
        j = n
    else:
        i = n

print(time - 2 * (i - 1) - 1)
