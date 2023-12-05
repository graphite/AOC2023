f = open('input5.txt')

seeds = [int(x) for x in f.readline().strip().split(': ')[1].split()]
f.readline()
f.readline()

def read_mapping(f):
    mapping = []
    l = f.readline().strip()
    while l:
        to, fr, r = [int(x) for x in l.split()]
        mapping.append((fr, to, r, to - fr))
        l = f.readline().strip()

    f.readline()
    mapping.sort(key = lambda x: x[0])
    return mapping

def apply_mapping(mapping, seeds):
    output = []
    for s in seeds:
        for fr, to, r, sh in mapping:
            if s > fr and s < fr + r:
                output.append(s + sh)
                break
    return output

for i in range(7):
    mapping = read_mapping(f)
    seeds = apply_mapping(mapping, seeds)

print(min(seeds))
