f = open('input9.txt')

# Lazy solution for 21 only
pascal = [[1]]
for i in range(20):
    pascal.append([])
    pascal[-1].append(1)
    for j in range(i):
        pascal[-1].append(pascal[i][j] + pascal[i][j+1])
    pascal[-1].append(1)

for i in range(len(pascal)):
    sign = 1
    for j in range(len(pascal[i])):
        pascal[i][j] *= sign
        sign *= -1

n = 0
for l in f:
    entries = [int(x) for x in l.strip().split()]
    top = 0
    for i in range(len(entries) - 1):
        top += pascal[len(entries) - 1][i] * entries[i + 1]
    n += top * pascal[len(entries) - 1][-1] * -1

print(n)
