f = open('input19.txt')

flows = {}

P = {'x': 0, 'm': 1, 'a': 2, 's': 3}

n = 0
for l in f:
    l = l.strip()
    if not l:
        break
    name, rest = l[:-1].split('{')
    flows[name] = []
    actions = set()
    for step in rest.split(','):
        if ':' not in step:
            flows[name].append((None, step))
            actions.add(step)
            continue
        cond, action = step.split(':')
        actions.add(action)
        flows[name].append(((P[cond[0]], cond[1], int(cond[2:])), action))
    if len(actions) == 1:
        flows[name] = actions.pop()

def check(name, valid, acc):
    if name == 'A':
        acc.append(valid)
        return
    if name == 'R':
        return
    flow = flows[name]
    if type(flow) is str:
        if flow == 'A':
            acc.append(valid)
            return
        elif flow == 'R':
            return
        else:
            check(flow, valid, acc)
            return
    for cond, action in flow:
        if not cond:
            check(action, valid, acc)
            return
        v1 = [[a, b] for a, b in valid]
        v2 = [[a, b] for a, b in valid]
        if cond[1] == '<':
            v1[cond[0]][1] = cond[2] - 1
            v2[cond[0]][0] = cond[2]
        else:
            v1[cond[0]][0] = cond[2] + 1
            v2[cond[0]][1] = cond[2]
        a, b = v1[cond[0]]
        if a <= b:
            check(action, tuple((a, b) for a, b in v1), acc)
        a, b = v2[cond[0]]
        if a > b:
            break
        valid = tuple((a, b) for a, b in v2)

acc = []
check('in', ((1, 4000), (1, 4000), (1, 4000), (1, 4000)), acc)
n = 0
for a, b, c, d in acc:
    n += (a[1] - a[0] + 1) * (b[1] - b[0] + 1) * (c[1] - c[0] + 1) * (d[1] - d[0] + 1)

print(n)
