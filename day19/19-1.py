f = open('input19.txt')

flows = {}

def gt(a, b):
    return a > b

def lt(a, b):
    return a < b

FUNC = {'>': gt, '<': lt}

for l in f:
    l = l.strip()
    if not l:
        break
    name, rest = l[:-1].split('{')
    flows[name] = []
    for step in rest.split(','):
        if ':' not in step:
            flows[name].append((None, step))
            continue
        cond, action = step.split(':')
        flows[name].append(((cond[0], FUNC[cond[1]], int(cond[2:])), action))

n = 0
for l in f:
    l = l.strip()
    part = {x[0]: int(x[2:]) for x in l[1:-1].split(',')}
    flow = 'in'
    while 1:
        if flow == 'R':
            break
        if flow == 'A':
            n += sum(part.values())
            break
        for cond, action in flows[flow]:
            if not cond:
                flow = action
                break
            if cond[1](part[cond[0]], cond[2]):
                flow = action
                break

print(n)
