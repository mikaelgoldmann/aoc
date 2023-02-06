import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def parse(line):
    a, b = line.split()
    return (a, int(b))


def get_moves():
    lines = get_lines()
    return [parse(x) for x in lines]


def mv(h, d):
    r, c = h
    if d == 'U':
        return r - 1, c
    if d == 'D':
        return r + 1, c
    if d == 'L':
        return r, c - 1
    assert d == 'R'
    return r, c + 1


def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def follow(h, t):
    if h == t:
        return t
    hr, hc = h
    tr, tc = t
    if abs(hc - tc) > 1 or  abs(hr - tr) > 1:
        tc += sign(hc - tc)
        tr += sign(hr - tr)
    return tr, tc


def travel(moves, num_knots):
    knots = [(0, 0) for i in range(num_knots)]
    vis = set()
    vis.add(knots[-1])
    for move in moves:
        d, n = move
        for i in range(n):
            knots[0] = mv(knots[0], d)
            for i in range(num_knots - 1):
                knots[i + 1] = follow(knots[i], knots[i + 1])
            vis.add(knots[-1])
    return len(vis)


if __name__ == '__main__':
    moves = get_moves()

    print("part 1")
    print(travel(moves, 2))


    print()
    print("part 2")
    print(travel(moves, 10))
