f = open('input5.txt')

s = [int(x) for x in f.readline().strip().split(': ')[1].split()]
seeds = []
for i in range(len(s) // 2):
    seeds.append((s[i*2], s[i*2] + s[i*2+1]))
#print(seeds)
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
            #print(fr,to,r,sh)
            #print(s)
            if s[0] >= fr and s[0] < fr + r:
                if s[1] > fr + r - 1:
                    output.append((s[0] + sh, to + r - 1))
                    s = (to + r - sh, s[1])
                    #print(s)
                else:
                    output.append((s[0] + sh, s[1] + sh))
                    s = ()
                    break
        if s:
            output.append(s)
        #print(output)
    return output

for i in range(7):
    #print('-------')
    mapping = read_mapping(f)
    seeds = apply_mapping(mapping, seeds)

print(min(seeds))
