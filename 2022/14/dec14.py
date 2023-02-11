import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def parse_line(line: str, rocks: set):
    parts = line.split(' -> ')
    pts = []
    for p in parts:
        x, y = p.split(',')
        pts.append((int(x), int(y)))
    for i in range(len(pts) - 1):
        a, b = pts[i]
        c, d = pts[i + 1]
        assert a == c or b == d
        rocks.add((a, b))
        rocks.add((c, d))
        if a == c:
            if b < d:
                for y in range(b, d):
                    rocks.add((a, y))
            else:
                for y in range(d, b):
                    rocks.add((a, y))
        else:
            if a < c:
                for x in range(a, c):
                    rocks.add((x, b))
            else:
                for x in range(c, a):
                    rocks.add((x, b))


def drop(sand, rocks, x, y, maxy):
    if (x, y) in sand:
        return
    if y == maxy:
        return
    if (x, y + 1) not in sand.union(rocks):
        drop(sand, rocks, x, y + 1, maxy)
    elif (x - 1, y + 1) not in sand.union(rocks):
        drop(sand, rocks, x - 1, y + 1, maxy)
    elif (x + 1, y + 1) not in sand.union(rocks):
        drop(sand, rocks, x + 1, y + 1, maxy)
    else:
        sand.add((x, y))


def drop2(sand, rocks, x, y, maxy):
    if y > maxy:
        print("wtf")
    if (x, y) in sand:
        return
    if y == maxy - 1:
        print('bottom', x, y)
        sand.add((x, y))
        return
    if (x, y + 1) not in sand and (x, y + 1) not in rocks:
        drop2(sand, rocks, x, y + 1, maxy)
    elif (x - 1, y + 1) not in sand and (x - 1, y + 1) not in rocks:
        drop2(sand, rocks, x - 1, y + 1, maxy)
    elif (x + 1, y + 1) not in sand and (x + 1, y + 1) not in rocks:
        drop2(sand, rocks, x + 1, y + 1, maxy)
    else:
        sand.add((x, y))


if __name__ == '__main__':
    sys.setrecursionlimit(1000)
    rocks = set()
    for line in get_lines():
        parse_line(line, rocks)
    print("rocks", rocks)
    maxy = max(y for x, y in rocks)
    sand = set()

    while True:
        n = len(sand)
        drop(sand, rocks, 500, 0, maxy)
        if n == len(sand):
            break

    print("part 1")
    print(len(sand))
    print()

    sand = set()
    while (500, 0) not in sand:
        drop2(sand, rocks, 500, 0, maxy + 2)


    print("part 2")
    print(len(sand))
