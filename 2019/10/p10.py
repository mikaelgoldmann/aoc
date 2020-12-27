import sys
import math
from collections import deque

def read_puzzles(inp=sys.stdin):
    ps = []
    p = []
    for line in inp:
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
    mc, mr = -1, -1
    for r in range(nr):
        for c in range(nc):
            if p[r][c] == '#':
                seen = count_seen(r, c, p)
                if mx < seen:
                    mx = seen
                    mc = c
                    mr = r
    return mx, mr, mc


with open(sys.argv[1]) as f:
    puzzles = read_puzzles(f)


def around(mr, mc):
    def key(r, c):
        assert r != mr or c != mc
        dst2 = (mr - r)**2 + (mc - c)**2
        if mc == c:
            angle = 0 if r < mr else math.pi
        elif r == mr:
            angle = math.pi / 2 if c > mc else 3 * math.pi / 2
        else:
            alpha = math.atan(abs(c - mc) / abs(r - mr))
            if r > mr:
                if c < mc:  # upper right
                    angle = alpha
                else:  # lower right
                    angle = math.pi - alpha
            else:
                if c > mc:  # lower left
                    angle = math.pi + alpha
                else:  # upper left
                    angle = 2 * math.pi - alpha
        return (angle, dst2)
    return key


def solve2(p, mr, mc):
    points = []
    for r in range(len(p)):
        for c in range(len(p[0])):
            if r == mr and c == mc:
                continue
            if p[r][c] == '#':
                points.append((r, c))
    key_fun = around(mr, mc)
    points = sorted(points, key=lambda x: key_fun(x[0], x[1]))
    last = None, None
    last_key = (None, None)
    num = 0
    pts = deque()
    while num < 200:
        if not(pts):
            pts = deque(points)
            points = []
            last_key = None, None
        r, c = pts.popleft()
        key = key_fun(r, c)
        if last_key[0] == key[0]:
            points.append((r, c))
        else:
            last = r, c
            num += 1
            print("step", num, "pos", c, r)
        last_key = key
    return last


for p in puzzles:
    print()
    mx, mr, mc = solve1(p)
    print(mr, mc)
    print("part 1", mx)
    r, c = solve2(p, mr, mc)
    print("part 2", c * 100 + r)
