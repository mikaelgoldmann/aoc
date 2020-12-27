import sys


def read_puzzles():
    ps = []
    p = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            ps.append(p)
            p = []
        else:
            p.append(line)
    ps.append(p)
    return ps


def gcd(a, b):
    if a < 0:
        return gcd(-a, b)
    if b < 0:
        return gcd(a, -b)
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def can_see(r0, c0, r1, c1, p):
    dr = r1 - r0
    dc = c1 - c0
    d = gcd(dr, dc)
    dr = dr // d
    dc = dc // d
#    print("can_see", r0, c0, r1, c1, dr, dc)
    r = r0
    c = c0
    while r != r1 or c != c1:
        r += dr
        c += dc
#        print (r, c)
        if p[r][c] == '#':
            break
#    print("can_see break", r0, c0, r1, c1, r, c)
    if r == r1 and c == c1:        
#        print("seen")
        return True
#    print("nope")
    return False


def count_seen(r0, c0, p):
    nc = len(p[0])
    nr = len(p)
    m = 0
    for r in range(nr):
        for c in range(nc):
            if r == r0 and c == c0:
                continue
            if p[r][c] == '#' and can_see(r0, c0, r, c, p):
                m += 1
#    print("count_seen", r0, c0, m)
    return m



def solve1(p):
    nc = len(p[0])
    nr = len(p)
    mx = 0
    for r in range(nr):
        for c in range(nc):
            if p[r][c] == '#':
                mx = max(mx, count_seen(r, c, p))
    return mx


puzzles = read_puzzles()


for p in puzzles:
    print()
    print("part 1", solve1(p))
