from math import gcd

f = open('input20.txt')

FUNCS = {}

STACK = []

GATE = ''

def broadcast(beam, name, _):
    func = FUNCS[name]
    for t in func['t']:
        STACK.append((beam, t, name))

def flip(beam, name, _):
    if beam:
        return
    func = FUNCS[name]
    out = not func['s']
    func['s'] = out
    for t in func['t']:
        STACK.append((out, t, name))

def conj(beam, name, fr):
    func = FUNCS[name]
    func['s'][fr] = beam
    out = False
    for s in func['s'].values():
        if not s:
            out = True
            break
    for t in func['t']:
        STACK.append((out, t, name))

def rx(_, __, ___):
    pass

for l in f:
    name, outs = l.strip().split(' -> ')
    outs = outs.split(', ')
    if 'rx' in outs:
        GATE = name[1:]
    if name[0] == '%':
        FUNCS[name[1:]] = {
            't': outs,
            's': False,
            'f': flip,
        }
    elif name[0] == '&':
        FUNCS[name[1:]] = {
            't': outs,
            's': {},
            'f': conj,
        }
    else:
        FUNCS[name] = {
            't': outs,
            'f': broadcast,
        }

FUNCS['rx'] = {'f': rx, 't': []}

for f, v in FUNCS.items():
    for t in v['t']:
        if FUNCS[t]['f'] == conj:
            FUNCS[t]['s'][f] = False

pregates = set(FUNCS[GATE]['s'].keys())
cycles = {}

n = 0
while len(cycles) != len(pregates):
    n += 1
    STACK = [(False, 'broadcaster', '')]
    while STACK:
        beam, to, fr = STACK.pop(0)
        if not beam and to in pregates:
            cycles[to] = n
        FUNCS[to]['f'](beam, to, fr)

n = 1
for i in cycles.values():
    n = n * i // gcd(n, i)

print(n)
