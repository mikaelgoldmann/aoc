import sys

x = [(y[0], int(y[1:].strip())) for y in sys.stdin]


dirs = 'ENWS'


pos = (0, 0)
dp = dict(E=(1,0), N=(0,1), W=(-1, 0), S=(0, -1))

def move(pos, n, direction):
    d1 = dp[direction]
    return (pos[0] + n * d1[0], pos[1] + n * d1[1])


def turn(d, lr, n):
    assert n in (90, 180, 270)
    if lr == 'R':
        n = 360 - n
    n = n // 90
    return (d + n) % 4
   
d = 0
for y, n in x:
    if y == 'F':
        pos = move(pos, n, dirs[d])
    elif y in dirs:
        pos = move(pos, n, y)
    elif y in 'LR':
        d = turn(d, y, n)
    else:
        assert False
    print (dirs[d], pos)

print("part 1", abs(pos[0]) + abs(pos[1]))


def lrot(v):
    x, y = v
    return (-y, x)

def lrotn(v, n):
    for i in range(n):
        v = lrot(v)
    return v

def rotate(wp, lr, n):
    assert n in (90, 180, 270)
    if lr == 'R':
        n = 360 - n
    n = n // 90
    return lrotn(wp, n)

wp = (10, 1)
pos = (0, 0)

def move2(p, w, n):
    return (p[0] + w[0] * n, p[1] + w[1] * n)

for y, n in x:
    if y == 'F':
        pos = move2(pos, wp, n)
    elif y in dirs:
        wp = move(wp, n, y)
    elif y in 'LR':
        wp = rotate(wp, y, n)
    else:
        assert False

print("part 2", abs(pos[0]) + abs(pos[1]))
