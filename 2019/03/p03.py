import sys

def parse(line):
    items = line.strip().split(',')
    return [(i[0], int(i[1:])) for i in items]

lines = [ parse(x) for x in sys.stdin ]


def delta(op):
    if op == 'U':
        return 0, 1
    if op == 'D':
        return 0, -1
    if op == 'L':
        return -1, 0
    if op == 'R':
        return 1, 0


def pos(l0):
    x, y = 0, 0
    p = [(0, 0)]
    for op, d in l0:
        dx, dy = delta(op)
        for i in range(d):
            x += dx
            y += dy
            p.append((x, y))    
    return p

def solve(l1, l2):
    pos1 = pos(l1)
    pos2 = pos(l2)
    ix = set(pos1).intersection(set(pos2))
#    print(pos1)
#    print(pos2)
#    print(ix)
#    print()
    return sorted(ix, key=lambda p: abs(p[0]) + abs(p[1]))


for i in range(0, len(lines), 2):
    l1 = lines[i]
    l2 = lines[i + 1]
    s = solve(l1, l2)
    print("part1", abs(s[1][0]) + abs(s[1][1]))


def d(ps):
    d1 = {}
    for i, (x, y) in enumerate(ps):
        if (x, y) not in d1:
            d1[(x, y)] = i
    return d1


def solve2(l1, l2):
    pos1 = pos(l1)
    pos2 = pos(l2)
    d1 = d(pos1)
    d2 = d(pos2)
    ix = set(d1.keys()).intersection(set(d2.keys()))
    opt = None
    for x, y in ix:
        if x == 0 and y == 0:
            continue
        s = d1[(x, y)] + d2[(x, y)]
        if opt is None or s < opt:
            opt = s
    return opt


for i in range(0, len(lines), 2):
    l1 = lines[i]
    l2 = lines[i + 1]
    s = solve2(l1, l2)
    print("part2", s)
